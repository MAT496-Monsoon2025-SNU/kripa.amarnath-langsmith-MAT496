
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate


HF_EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def get_hf_embeddings(model_name: str = HF_EMBEDDING_MODEL_NAME):
    """
    Initializes and returns a HuggingFaceEmbeddings object.
    """
    return HuggingFaceEmbeddings(model_name=model_name)

def get_hf_vector_db_retriever(
    embedding_model_name: str = HF_EMBEDDING_MODEL_NAME,
    vector_db_path: str = "faiss_index_hf",
    document_path: str = "state_of_the_union.txt" 
):
    """
    Initializes and returns a FAISS vector store retriever using Hugging Face embeddings.
    If the vector DB doesn't exist, it creates it from a sample document.
    """
    embeddings = get_hf_embeddings(model_name=embedding_model_name)

    if not os.path.exists(vector_db_path):
        print(f"Creating new FAISS vector database at {vector_db_path} with Hugging Face embeddings...")
        if not os.path.exists(document_path):
            with open(document_path, "w") as f:
                f.write("The quick brown fox jumps over the lazy dog. This is a sample document for testing Hugging Face embeddings and FAISS vector store functionality.")
                f.write("\n\nLangChain is a framework for developing applications powered by language models. It enables applications that are context-aware, reason, and can act.")
                f.write("\n\nHugging Face provides open-source models for various NLP tasks, including embeddings. These models can be run locally or via their inference API.")

        loader = TextLoader(document_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        db = FAISS.from_documents(docs, embeddings)
        db.save_local(vector_db_path)
        print("FAISS vector database created.")
    else:
        print(f"Loading FAISS vector database from {vector_db_path} with Hugging Face embeddings...")
        db = FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)
        print("FAISS vector database loaded.")

    return db.as_retriever()

RAG_PROMPT = PromptTemplate.from_template("""You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the latest question in the conversation.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Conversation history:
{conversation}
Question: {question}
Context: {context}
""")