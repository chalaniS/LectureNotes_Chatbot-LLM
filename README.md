# 📚 CTSE Lecture Notes Chatbot – RetrievalQA with LLaMA3 (Ollama + LangChain)

This project presents a local, offline chatbot designed to assist students by answering questions based on lecture notes from the "Current Trends in Software Engineering (SE4010)" module at SLIIT. Leveraging Retrieval-Augmented Generation (RAG) techniques, the chatbot ensures accurate and contextually relevant responses without the need for internet connectivity or external API keys.</br></br>
![Screenshot 2025-05-07 175421](https://github.com/user-attachments/assets/22b05619-c0f7-4aa4-b07f-165f9f244e61)



## 🚀 Features

* **Retrieval-Augmented Generation (RAG):** Combines information retrieval with generative models to provide precise answers.
* **Local LLM Integration:** Utilizes local Large Language Models (LLMs) like LLaMA3 or TinyLlama via Ollama, ensuring data privacy and offline functionality.
* **Efficient Document Retrieval:** Employs ChromaDB for rapid vector-based retrieval of lecture content.
* **User-Friendly Interface:** Built with Streamlit for an intuitive and interactive user experience.
* **No External Dependencies:** Operates without the need for API keys or internet access.([GitHub][1])

## 🗂️ Project Structure

```
LectureNotes_Chatbot-LLM/
├── app.py                             # Streamlit web application
├── chatbot.py                         # Core chatbot logic
├── requirements.txt                   # Python dependencies
├── ctse_lecture_notes.pdf             # Lecture notes in PDF format
├── llama3/
│   ├── lecsnote-chatbot-SimpleRetrievalQA-llama3.ipynb
│   └── lecsnote-chatbot-ConversationalRetrievalChain-llama3.ipynb
└── README.md                          # Project documentation
```

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chalaniS/LectureNotes_Chatbot-LLM.git
cd LectureNotes_Chatbot-LLM
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Set Up Ollama

Follow the official Ollama installation guide: [https://ollama.com](https://ollama.com)

Once installed, download the desired model- TinyLlama:

```bash
ollama list
```

```bash
ollama pull llamatyne
```

```bash
ollama run llamatyne
```

## 📄 Preparing Lecture Notes

Ensure your lecture notes are in PDF format and named `ctse_lecture_notes.pdf`. Place this file in the root directory of the project.

## 🚀 Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The chatbot interface will open in your default web browser.([GitHub][1])

## 🧠 How It Works

1. **Document Ingestion:** The PDF lecture notes are converted into text and segmented into manageable chunks.
2. **Embedding Generation:** Each text chunk is transformed into a vector representation using Sentence Transformers.
3. **Vector Storage:** These vectors are stored in ChromaDB, facilitating efficient similarity searches.
4. **Query Handling:** When a user poses a question, the system retrieves the most relevant text chunks from ChromaDB.
5. **Answer Generation:** The retrieved information is passed to the local LLM via LangChain, which generates a coherent and contextually appropriate response.([GitHub][2])

## 📓 Notebooks

The `llama3/` directory contains Jupyter notebooks that demonstrate different retrieval strategies:

* **SimpleRetrievalQA:** A straightforward retrieval-based question-answering approach.
* **ConversationalRetrievalChain:** An advanced method that maintains conversational context across multiple queries.

## 📌 Notes

* **Model Selection:** You can switch between different LLMs (e.g., LLaMA3, TinyLlama) by modifying the model name in the `app.py` file.
* **Data Privacy:** All processing is done locally, ensuring that your data remains private.
* **Customization:** Feel free to adapt the chatbot for other courses or datasets by replacing the lecture notes PDF.



