import streamlit as st
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
import uuid
from langgraph_rag_backend import (
    chatbot,
    ingest_pdf,
    retrieve_all_threads,
    thread_document_metadata,
)


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

    st.session_state['chat_threads'] = retrieve_all_threads()

if 'chat_names' not in st.session_state:
    st.session_state['chat_names'] = {}

if "ingested_docs" not in st.session_state:
    st.session_state["ingested_docs"] = {}

add_chat_thread(st.session_state['thread_id'])

thread_key = str(st.session_state['thread_id'])
thread_docs = st.session_state['ingested_docs'].setdefault(thread_key, {})
threads = st.session_state['chat_threads'][::-1]
selected_thread = None

# ************** Sidebar Ui ********************
st.sidebar.title("LangGraph RAG Chatbot")
st.markdown(f'**Thread ID** `{thread_key}`')

if st.sidebar.button("New Chat", use_container_width=True):
    reset_chat()
    st.rerun()

if thread_docs:
    latest_doc = list(thread_docs.values())[-1]
    st.sidebar.success(
        f'Using `{latest_doc.get('filename')}`'
        f'({latest_doc.get('chunks')} chunks from {latest_doc.get('documents')} pages)'
    )
else:
    st.sidebar.info('No PDF indexed yet.')

uploaded_pdf = st.sidebar.file_uploader('upload a pdf for this chat', type=['pdf'])
if uploaded_pdf:
    if uploaded_pdf.name in thread_docs:
        st.sidebar.info(f'`{uploaded_pdf.name}` already processed for this chat.')
    else:
        with st.sidebar.status("Indexing PDF...", expanded=True) as status_box:
            summary = ingest_pdf(
                uploaded_pdf.getvalue(),
                thread_id=thread_key,
                filename=uploaded_pdf.name,
            )
            thread_docs[uploaded_pdf.name] = summary
            status_box.update(label='PDF indexed', state='complete', expanded=False)

st.sidebar.subheader("Past Conversations")
if not threads:
    st.sidebar.write("No Past Conversation yet.")
else:
    for thread_id in threads:
        if st.sidebar.button(str(thread_id), key=f'side-thread-{thread_id}'):
            selected_thread = thread_id

# ***************** Main Ui ************************
st.title("Multi Utility Chatbot")
st.subheader("Tools: web search, calculator, rag"
"")
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
    CONFIG = {
        'configurable': {'thread_id': thread_key},
        'metadata': {'thread_id': thread_key},
        'run_name': 'chat_turn'
        }

    with st.chat_message("AI"):
        tools_used = []

        def ai_only_msg():
            for message_chunk, _ in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            ):

                
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_msg())

        if tools_used:
            st.caption(f"Tools used: {', '.join(tools_used)}")
        
    st.session_state['msg_history'].append({'role':'Ai', 'content':ai_message})

    doc_meta = thread_document_metadata(thread_key)
    if doc_meta:
        st.caption(
            f"Document indexed: {doc_meta.get('filename')} "
            f"(chunks: {doc_meta.get('chunks')}, pages: {doc_meta.get('documents')})"
        )

st.divider()

if selected_thread:
    st.session_state["thread_id"] = selected_thread
    messages = load_conversation(selected_thread)

    temp_messages = []
    for msg in messages:
        role = "user" if isinstance(msg, HumanMessage) else "assistant"
        temp_messages.append({"role": role, "content": msg.content})
    st.session_state["message_history"] = temp_messages
    st.session_state["ingested_docs"].setdefault(str(selected_thread), {})
    st.rerun()
