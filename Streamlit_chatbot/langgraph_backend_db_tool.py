from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langgraph.graph import add_messages
from langgraph.prebuilt import tool_node, tools_condition, ToolNode
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests

load_dotenv()
llm_model = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    temperature=0.7
)

## tools function 
search_tool = DuckDuckGoSearchRun(region="us-en")

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


## combine tools in tool node
tools = [search_tool, calculator]
# bind tool with llm
llm_tool = llm_model.bind_tools(tools)

tool_node = ToolNode(tools)

## define state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state:ChatState):
    """LLM node that may answer or request a tool call."""
    # take user query from state
    messages = state['messages']
    response = llm_tool.invoke(messages)


    # sent to llm 
    # response = llm_model.invoke(messages)

    # response store in state
    return {'messages': [response]}



# define the graph and checkpoint
conn = sqlite3.connect(database='chatbot_db', check_same_thread=False)

checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

# add node
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)

#add edge
graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')
graph.add_edge('chat_node' , END)

chatbot = graph.compile(checkpointer=checkpointer)

## check threads in sqlite db
def get_all_threads():
    all_threads = set()
    for cp in checkpointer.list(None):
        all_threads.add(cp.config['configurable']['thread_id'])
    
    return list(all_threads)