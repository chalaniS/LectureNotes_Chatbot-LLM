
# 📘 CTSE Lecture Notes Chatbot – RetrievalQA with LLaMA3 (Ollama + LangChain)

This project is a local, offline chatbot built using LangChain, ChromaDB, and Ollama (TinyLlama or LLaMA3). It allows users to ask questions based on lecture notes from the Current Trends in Software Engineering (SE4010) module at SLIIT.

🧠 Features

* Uses Retrieval-Augmented Generation (RAG) for accurate QA
* Powered by local LLM (Ollama + LLaMA3 / TinyLlama) – no API keys needed
* Loads lecture notes from .txt file and embeds with Sentence Transformers
* Uses ChromaDB for fast vector-based retrieval
* Streamlit UI for easy question-answer interaction

📁 File Structure

your\_project/<br>
│<br>
├── app.py                            # Streamlit web interface<br>
├── ctse\_lecture\_notes.txt            # Your lecture notes (as plain text)<br>
├── llama3/<br>
│   └── lecsnote-chatbot-SimpleRetrievalQA-llama3.ipynb   		# Notebook version<br>
│   └── lecsnote-chatbot-ConversationalRetrievalChain-llama3.ipynb   	# Notebook version<br>
├── chroma\_db/                        # (auto-generated vector store on first run)<br>
└── requirements.txt                  # Python dependencies<br>

⚙️ Requirements

* Python 3.8+
* Ollama installed and running locally
* Recommended: LLaMA3 or TinyLlama model pulled via Ollama

Install dependencies:

pip install -r requirements.txt

Start Ollama model:

ollama run llama3

▶️ Run the App

streamlit run app.py

Then open [http://localhost:8501](http://localhost:8501) in your browser.

📝 How It Works

1. TextLoader loads ctse\_lecture\_notes.txt
2. The text is split using RecursiveCharacterTextSplitter
3. Embeddings are created using sentence-transformers/all-MiniLM-L6-v2
4. Vectors are stored in ChromaDB
5. RetrievalQA fetches relevant chunks based on user query
6. Ollama (LLaMA3) generates a response

🧪 Dev Notes

* The notebook in llama3/ can be used for experiments.
* LLaMA3 and TinyLlama models tested via Ollama.
* Ideal for low-latency, offline academic use cases.

📚 References

* LangChain RAG Tutorial: [https://python.langchain.com/docs/tutorials/rag/](https://python.langchain.com/docs/tutorials/rag/)
* ChromaDB: [https://docs.trychroma.com/](https://docs.trychroma.com/)
* Ollama: [https://ollama.com/library/llama3](https://ollama.com/library/llama3)
* Sentence Transformers: [https://www.sbert.net/](https://www.sbert.net/)


