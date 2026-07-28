from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import List, TypedDict, Annotated
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio

load_dotenv()

llm = ChatOpenRouter(model='nvidia/nemotron-3-nano-30b-a3b:free')



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


tools = [calculator]

llm_with_tools = llm.bind_tools(tools)

# state
class ChatSate(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]


# define graph and nodes

def build_graph():

    # nodes
    async def chat_node(state:ChatSate):
        msg = state['messages']
        response = await llm_with_tools.ainvoke(msg)
        return {'messages':[response]}

    tool_node = ToolNode(tools)


    graph = StateGraph(ChatSate)
    graph.add_node('chat_node',chat_node)
    graph.add_node('tools', tool_node)

    # defining edges
    graph.add_edge(START, 'chat_node')
    graph.add_conditional_edges('chat_node', tools_condition)
    graph.add_edge('tools', 'chat_node')
    graph.add_edge('chat_node', END)

    chatbot = graph.compile()

    return chatbot


async def main():

    chatbot = build_graph()

    # execute graph
    start_state = {
        'messages' : [HumanMessage(content='Find the product of 123321 and 44 and give the answer like a indian mother.')]
    }

    result = await chatbot.ainvoke(start_state)

    print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())