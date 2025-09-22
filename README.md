Got it 👍 Here’s your **README.md** in a single continuous note-style text (no section breaks, you can paste it directly into your repo):

---

````markdown
# 📚 Local RAG Chatbot (Powered by Ollama + Streamlit)

This project is a Retrieval-Augmented Generation (RAG) chatbot that uses LangChain, Ollama, and ChromaDB to answer questions based on your local documents. It can load `.txt` and `.pdf` files from a documents folder, split text into smaller chunks, generate embeddings using HuggingFace (all-MiniLM-L6-v2), store them in ChromaDB, and query them through Ollama models like Mistral, Gemma, or Llama2 with an interactive Streamlit UI.

## Setup Instructions

Clone the repository:
```bash
git clone https://github.com/your-username/rag-chatbot-ollama.git
cd rag-chatbot-ollama
````

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama by downloading it from [https://ollama.ai/](https://ollama.ai/), then pull a model:

```bash
ollama pull mistral
```

Add your `.txt` or `.pdf` documents inside the `documents/` folder. Then start the chatbot with:

```bash
streamlit run app.py
```

## Project Structure

```
rag-chatbot-ollama/
│── app.py              # Main Streamlit app
│── documents/          # Folder containing .txt / .pdf files
│── chroma_db/          # Vector database (auto-created)
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

## Example

Ask something like:
❓ "Summarize the key points from my research paper in `documents/`"
🤖 The chatbot will respond with AI-generated answers based on your files.

## Dependencies

Python 3.9+, Streamlit, LangChain, LangChain-Community, Chroma, HuggingFace Transformers, Sentence-Transformers, Torch, PyPDF.

## Author

Created by [Nishk Dongre](https://github.com/nishk24)

```

