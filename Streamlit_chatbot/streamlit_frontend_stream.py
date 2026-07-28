import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

## st.session_state -- dict 
if 'msg_history' not in st.session_state:
    st.session_state['msg_history'] = []

for msg in st.session_state['msg_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

user_input = st.chat_input('Ask Question Here')

if user_input:

    # save the user msg in session state
    st.session_state['msg_history'].append({'role':'User', 'content':user_input})
    with st.chat_message('User'):
        st.text(user_input)

    # get llm answer

    # response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    with st.chat_message("AI"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]}, 
                config=CONFIG,
                stream_mode=
                'messages'
            )
        )
    st.session_state['msg_history'].append({'role':'Ai', 'content':ai_message})
