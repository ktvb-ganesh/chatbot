import os
from random import seed
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_core.tools import create_retriever_tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import streamlit as st



# wikipedia tools
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results =1, doc_content_chars_max=4000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
#arxiv tool
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results =1, doc_content_chars_max=4000)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
#search tool
search = DuckDuckGoSearchRun(name="Search")


st.title("LangChain Chatbot search engine")
st.sidebar.title("settings")
groq_api_key = st.sidebar.text_input("Enter your Groq API key", type="password")

session_id = st.sidebar.text_input("Enter your session id", value="default")


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello, I am a search engine. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]


if prompt := st.chat_input("Enter your prompt"):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=groq_api_key
    )

    tools = [wiki, arxiv, search]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant."
    )

    agent_with_memory = RunnableWithMessageHistory(
        agent,
        get_session_history,
        input_messages_key="messages",
    )

    with st.chat_message("assistant"):

        response = agent_with_memory.invoke(
            {"messages": prompt},
            config={"configurable": {"session_id": session_id}},
        )

        assistant_reply = response["messages"][-1].content

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply}
        )

        st.write(assistant_reply)