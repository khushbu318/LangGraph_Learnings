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
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message = response['messages'][-1].content
    st.session_state['msg_history'].append({'role':'Ai', 'content':ai_message})
    with st.chat_message("AI"):
        st.markdown(ai_message)