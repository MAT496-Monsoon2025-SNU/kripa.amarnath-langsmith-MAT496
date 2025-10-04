
import os
import faiss
import pickle
from langchain_community.document_loaders import SitemapLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore
import uuid

RAG_PROMPT = """
You are an AI assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know. Keep the answer concise.

Conversation:
{conversation}

Context:
{context}

Question:
{question}
"""

def get_vector_db_retriever(openai_api_key: str = None):
    """
    Initializes and returns a vector store retriever.
    If openai_api_key is provided, it will be used. Otherwise, it defaults
    to the OPENAI_API_KEY environment variable.
    """
    persist_path = "./langsmith_docs_rag_vectorstore"
    
    
    api_key_to_use = openai_api_key
    if api_key_to_use is None:
        api_key_to_use = os.getenv("OPENAI_API_KEY")
    
    if not api_key_to_use:
        raise ValueError(
            "OpenAI API key not provided and OPENAI_API_KEY environment "
            "variable is not set. Please provide a key or set the environment variable."
        )

    if os.path.exists(persist_path) and os.path.exists(os.path.join(persist_path, 'docstore.parquet')):
        print("Loading existing vector store...")
        embd = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=api_key_to_use)
        vectorstore = SKLearnVectorStore(embedding=embd, persist_path=persist_path, serializer="parquet")
        return vectorstore.as_retriever(lambda_mult=0)

    print("Creating new vector store from LangSmith documentation...")
    ls_docs_sitemap_loader = SitemapLoader(web_path="https://docs.smith.langchain.com/sitemap.xml", continue_on_failure=True)
    ls_docs = ls_docs_sitemap_loader.load() 

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(ls_docs)

    embd = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=api_key_to_use)

    vectorstore = SKLearnVectorStore.from_documents(
        documents=doc_splits,
        embedding=embd,
        persist_path=persist_path,
        serializer="parquet"
    )
    vectorstore.persist()
    print("Vector store created and persisted.")
    return vectorstore.as_retriever(lambda_mult=0)
