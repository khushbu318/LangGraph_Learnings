from __future__ import annotations

import os
import sqlite3
import tempfile
from typing import Annotated, Any, Dict, Optional, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_openrouter import ChatOpenRouter
# from langchain_openrouter import OpenRouterEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
import requests
from langchain_core.embeddings import Embeddings
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

# -------------------
# 1. LLM + Embeddings MODEL
# -------------------

llm = ChatOpenAI(
    model="nvidia/nemotron-3-nano-30b-a3b:free",   # or any OpenRouter model
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.9
)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

# -------------------
# 2. PDF retriever store (per thread)
# -------------------

_THREAD_RETRIEVERS: Dict[str, Any] = {}
_THREAD_METADATA: Dict[str, Any] = {}

def _get_retriever(thread_id: Optional[str]):
    """ Fetch the retriever for a thread if available """
    if thread_id and thread_id in _THREAD_RETRIEVERS:
        return _THREAD_RETRIEVERS[thread_id]
    return None

def ingest_pdf(file_bytes: bytes, thread_id: str, filename: Optional[str] = None) -> dict: 
    """
    Build a FAISS retriever for the uploaded PDF and store it for the thread.
    Return a summary dict that can be surfaced in the UI.
    """
    if not file_bytes:
        raise ValueError("NO bytes recieve for ingestion")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file_bytes)
        temp_path = temp_file.name

    try: 
        loader = PyPDFLoader(temp_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        vector_store = FAISS.from_documents(chunks, embeddings)

        retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})

        _THREAD_RETRIEVERS[str(thread_id)] = retriever
        _THREAD_METADATA[str(thread_id)] = {
            "filename": filename or os.path.basename(temp_path),
            "documents": len(docs),
            "chunks": len(chunks)
        }

        return {
            "filename": filename or os.path.basename(temp_path),
            "documents": len(docs),
            "chunks": len(chunks)
        }
    finally:
        # The FAISS store keeps copies of the text, so the temp file is safe to remove.
        try:
            os.remove(temp_path)
        except OSError:
            return {'error':'Error while removing temp_path file'}


# -------------------
# 3. Tools
# -------------------

search_tool = DuckDuckGoSearchRun(region='us-en')

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: addition, subtraction, multiplication, division
    """
    print("Calculator tool is used")

    try:
        operation = operation.lower()

        if operation in ('addition', '+', 'add'):
            res = first_num + second_num

        elif operation in ('subtraction', '-', 'sub'):
            res = first_num - second_num

        elif operation in ('multiplication', '*', 'x', 'mul', 'multiply'):
            res = first_num * second_num

        elif operation in ('division', 'div', '/'):
            if second_num == 0:
                return {'error': 'Division by zero is not allowed'}
            res = first_num / second_num

        else:
            return {'error': f'Unsupported operation {operation}'}

        return {
            'first_num': first_num,
            'second_num': second_num,
            'operation': operation,
            'result': res
        }

    except Exception as e:
        return {'error': str(e)}

@tool
def rag_tool(query: str, thread_id: Optional[str] = None) -> dict:
    """
    Retrieve relevant information from the uploaded pdf document for this chat thread.
    Always include the thread_id when calling this tool.
    """

    retriever = _get_retriever(thread_id)
    if retriever is None:
        return {
            "error": 'No Document Indexed for this chat. Upload a PDF first',
            "query": query
        }


    similar_chunks = retriever.invoke(query)

    context = [doc.page_content for doc in similar_chunks]
    metadata = [doc.metadata for doc in similar_chunks]

    return {
        'query': query,
        'context': context,
        'metadata': metadata,
        'source_file': _THREAD_METADATA.get(str(thread_id), {}).get("filename"),
    }

tools = [search_tool, calculator, rag_tool]
llm_with_tools = llm.bind_tools(tools)

# -------------------
# 4. State
# -------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# -------------------
# 5. Nodes
# -------------------
def chat_node(state: ChatStae, config=None):
    """ LLM nod that may answer or request a tool call."""
    thread_id = None
    if config and isinstance(config, dict):
        thread_id = config.get('configurable', {}).get('thread_id')

    system_message = SystemMessage(
        content=(
            F'You are a helpful assistant. For question about the uploded PDF, call the `rag_tool` and include the thread_id {thread_id}. You can also user the web search, calculator tools when helpful. If no document is available, ask the user to upload a PDF'
        )
    )

    messages = [system_message, *state['messages']]
    response = llm_with_tools.invoke(messages, config=config)
    return {'messages': [response]}

tool_node = ToolNode(tools)


# -------------------
# 6. Checkpointer
# -------------------
# define the graph and checkpoint
conn = sqlite3.connect(database='chatbot_db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# -------------------
# 7. Graph
# -------------------
graph = StateGraph(ChatState)

# add node
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)

#add edge
graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')

chatbot = graph.compile(checkpointer=checkpointer)

# -------------------
# 8. Helpers
# -------------------
## check threads in sqlite db
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_threads)


def thread_has_document(thread_id: str) -> bool:
    return str(thread_id) in _THREAD_RETRIEVERS


def thread_document_metadata(thread_id: str) -> dict:
    return _THREAD_METADATA.get(str(thread_id), {})


