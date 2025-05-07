import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# Load and embed documents, store in persistent ChromaDB
@st.cache_resource
def load_qa_chain():
    loader = TextLoader("ctse_lecture_notes.pdf", encoding="utf-8")
    docs = loader.load()

    # Split the documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Generate embeddings for the chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create and persist the Chroma vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    # Set up retriever and language model
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="llama3" or "tinyllama")  # Ensure Ollama is running with Llama3 or TinyLlama
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    return qa

# Streamlit page configuration
st.set_page_config(page_title="CTSE Chatbot", layout="wide")
st.title("📘 CTSE Lecture Notes Chatbot (LLama3 + LangChain)")

# Load QA chain
qa_chain = load_qa_chain()

# User query input field
user_query = st.text_input("Ask a question about CTSE or Software Engineering:")

# Display the answer based on user query
if user_query:
    try:
        answer = qa_chain.run(user_query)
        st.markdown("#### 🤖 Answer:")
        st.write(answer)
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
