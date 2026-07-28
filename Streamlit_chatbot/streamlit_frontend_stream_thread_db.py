import streamlit as st
from langgraph_backend_db_tool import *
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
import uuid

# ************ utility function ************

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_chat_thread(st.session_state['thread_id'])
    st.session_state['msg_history'] = []

def add_chat_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    CONFIG = {'configurable': {'thread_id': thread_id }}
    state = chatbot.get_state(config=CONFIG)

    return state.values.get('messages',[])
# ***************** session setup **************

## st.session_state -- dict
if 'msg_history' not in st.session_state:
    st.session_state['msg_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:

    st.session_state['chat_threads'] = get_all_threads()

if 'chat_names' not in st.session_state:
    st.session_state['chat_names'] = {}

add_chat_thread(st.session_state['thread_id'])

# ************** Sidebar Ui ********************
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversation")

for thread_id in st.session_state['chat_threads'][::-1]:
    label = st.session_state['chat_names'].get(str(thread_id), "Current Chat")
    if st.sidebar.button(label, key=str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'User'
            else:
                role = 'Ai'
            temp_messages.append({'role':role, 'content': msg.content})

        st.session_state['msg_history'] = temp_messages
        st.rerun()

# ***************** Main Ui ************************
for msg in st.session_state['msg_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

user_input = st.chat_input('Ask Question Here')

if user_input:

    # name the chat from the first message
    tid_key = str(st.session_state['thread_id'])
    if tid_key not in st.session_state['chat_names']:
        st.session_state['chat_names'][tid_key] = user_input[:40]

    # save the user msg in session state
    st.session_state['msg_history'].append({'role':'User', 'content':user_input})
    with st.chat_message('User'):
        st.text(user_input)

    # get llm answer
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id'] }}

    with st.chat_message("AI"):
        tools_used = []

        def ai_only_msg():
            for msg_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            ):
                if isinstance(msg_chunk, ToolMessage) and msg_chunk.name:
                    tools_used.append(msg_chunk.name)
                    print(f"Tool used: {msg_chunk.name}")
                elif isinstance(msg_chunk, AIMessage) and msg_chunk.content:
                    yield msg_chunk.content

        ai_message = st.write_stream(ai_only_msg())

        if tools_used:
            st.caption(f"Tools used: {', '.join(tools_used)}")
        
    st.session_state['msg_history'].append({'role':'Ai', 'content':ai_message})
