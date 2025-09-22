Got it 👍 I’ll remove the virtual environment part and keep the `README.md` simple.
Here’s the updated version for your GitHub:

---

# 📚 Local RAG Chatbot (Powered by Ollama)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with **Streamlit, LangChain, Ollama, and ChromaDB**.
It allows you to upload `.txt` and `.pdf` documents, stores them in a local vector database, and then queries them using a local LLM (via Ollama).

---

## 🚀 Features

* Load documents (`.txt` and `.pdf`) from a folder.
* Split text into chunks for better retrieval.
* Store embeddings in **ChromaDB**.
* Use **HuggingFace embeddings** for vector storage.
* Query documents using **Ollama models** like `mistral`, `gemma:2b`, or `llama2`.
* User-friendly **Streamlit interface**.

---

## 📂 Project Structure

```
.
├── app.py               # Main Streamlit app
├── documents/           # Folder containing .txt / .pdf documents
├── chroma_db/           # Local vector database (auto-generated)
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/rag-chatbot.git
   cd rag-chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > If you don’t have a `requirements.txt`, install manually:

   ```bash
   pip install streamlit langchain chromadb sentence-transformers pypdf
   ```

3. **Install Ollama**
   Download and install Ollama from 👉 [https://ollama.ai](https://ollama.ai)

4. **Pull a model (example: mistral)**

   ```bash
   ollama pull mistral
   ```

---

## ▶️ Usage

1. Add your documents (`.txt` or `.pdf`) inside the `documents/` folder.

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the link shown in the terminal (usually `http://localhost:8501`).

4. Ask questions about your documents in the chat input box.

---

## 🧠 Example Query

* Upload a research paper PDF.
* Ask: *“Summarize the key findings of this paper.”*
* The chatbot retrieves relevant text chunks and provides an answer using your local LLM.

---

## 🛠️ Tech Stack

* **Streamlit** → UI
* **LangChain** → RAG pipeline
* **ChromaDB** → Vector database
* **HuggingFace** → Embeddings (`all-MiniLM-L6-v2`)
* **Ollama** → Local LLMs (Mistral, Gemma, Llama2, etc.)

---

## 📌 Notes

* All data stays **local** on your machine.
* Works offline after initial setup.
* You can switch Ollama models by updating:

  ```python
  llm = Ollama(model="mistral")
  ```

---

