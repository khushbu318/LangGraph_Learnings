from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import List, TypedDict, Annotated
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from typing import cast
import sys

load_dotenv()

llm = ChatOpenRouter(model='nvidia/nemotron-3-nano-30b-a3b:free')

## mcp client for local FastMCP server
client = MultiServerMCPClient(
    cast(dict, {
        "calci": {
            'transport': 'stdio',
            'command': sys.executable,
            'args': ['09_langgraph_mcp_server.py']
        },
        "parallel": {
            "transport": "http",
            "url": "https://search.parallel.ai/mcp"
        }
    })
)



# state
class ChatSate(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]


# define graph and nodes

async def build_graph():

    tools = await client.get_tools()
    # print("Calci mcp server Tools", tools)

    llm_with_tools = llm.bind_tools(tools)


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

    chatbot = graph.compile()

    return chatbot


async def main():

    chatbot = await build_graph()

    # execute graph
    start_state = {
        'messages' : [HumanMessage(content='What is latest news about indian protest of CJP and list 2 good news and 2 bad news.')]
    }

    result = await chatbot.ainvoke(start_state)

    for msg in result["messages"]:
        print(type(msg))
        print(msg)
        print("-" * 50)

    print(result['messages'][-1].content)

if __name__ == '__main__':
    asyncio.run(main())