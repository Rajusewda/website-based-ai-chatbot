import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama

from utils.validators import check_website_access, URLValidationError
from crawler.loader import load_website
from crawler.cleaner import clean_html
from processing.chunker import chunk_text
from processing.embeddings import EmbeddingModel
from vectorstore.chroma_db import ChromaVectorStore
from chatbot.retriever import build_context
from chatbot.qa_chain import QAChain
import os

load_dotenv()

st.set_page_config(page_title="Website Chatbot", layout="wide")
st.title("Website-Based AI Chatbot")

if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔹 URL input ALWAYS visible
url = st.text_input("Enter website URL")
st.caption("The chatbot will only answer questions based on the indexed website.")
st.caption("Powered by local LLaMA-3 (Ollama). No external APIs used.")

if st.button("Index Website"):
    try:
        check_website_access(url)

        pages = load_website(url)
        documents = []

        for page in pages:
            text = clean_html(page["html"])
            docs = chunk_text(text, page["url"], page["title"])
            documents.extend(docs)

        embedder = EmbeddingModel()
        vectors = ChromaVectorStore()

        texts = [doc["content"] for doc in documents]
        embeddings = embedder.embed_texts(texts)
        vectors.add_documents(documents, embeddings)

        st.session_state.indexed = True
        st.success("Website indexed successfully")

    except URLValidationError as e:
        st.error(str(e))

# 🔹 Chat section (guarded)
if not st.session_state.indexed:
    st.info("Please index a website before asking questions.")
else:
    question = st.chat_input("Ask a question about the website")

    if question:
        embedder = EmbeddingModel()
        vectors = ChromaVectorStore()

        query_embedding = embedder.embed_query(question)
        results = vectors.similarity_search(query_embedding)

        context = build_context(results)

        llm = Ollama(
        model="llama3",
        temperature=0
        )
        qa = QAChain(llm)

        answer = qa.answer(question, context)

        st.session_state.chat_history.append(
            {"role": "user", "content": question}
        )
        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

    for msg in st.session_state.chat_history:
        st.chat_message(msg["role"]).write(msg["content"])