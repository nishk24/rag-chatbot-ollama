import streamlit as st
from pathlib import Path
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

# Step 1: Load documents from folder
docs_path = Path("documents")
documents = []

for file in docs_path.glob("*"):
    if file.suffix == ".txt":
        loader = TextLoader(str(file))
    elif file.suffix == ".pdf":
        loader = PyPDFLoader(str(file))
    else:
        continue
    documents.extend(loader.load())

# Step 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Step 3: Embed and store in Chroma
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma.from_documents(chunks, embedding, persist_directory="chroma_db")
vector_db.persist()

# Step 4: Load local model from Ollama
llm = Ollama(model="mistral")  # You can use "gemma:2b", "llama2" too

# Step 5: Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_db.as_retriever(),
    chain_type="stuff"
)

# Step 6: Streamlit UI
st.title("📚 Local RAG Chatbot (Powered by Ollama)")
query = st.text_input("Ask a question based on your documents:")

if query:
    answer = qa_chain.run(query)
    st.write("🤖 Answer:", answer)