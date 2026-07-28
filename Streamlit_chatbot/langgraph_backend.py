from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
llm_model = ChatOpenRouter(
    model="nvidia/nemotron-3-nano-30b-a3b:free",
    temperature=0.8
)
## define state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state:ChatState):
    # take user query from state
    messages = state['messages']

    # sent to llm 
    response = llm_model.invoke(messages)

    # response store in state
    return {'messages': [response]}


# define the graph and checkpoint

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

# add node

graph.add_node('chat_node', chat_node)

#add edge
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpointer)

