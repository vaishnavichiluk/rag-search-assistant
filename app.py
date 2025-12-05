import os
os.environ["OPENAI_API_KEY"] = "open api key"

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_core.runnables import RunnablePassthrough


# loading documets that are required for this project
def load_documents():
    docs = []
    for file in os.listdir("data"):
        path = os.path.join("data", file)
        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt"):
            docs.extend(TextLoader(path).load())
    return docs

# Build vector embeddings
def build_vector_store():
    docs = load_documents()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("vector_index")
    return vector_store

# Load vector store
def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("vector_index", embeddings, allow_dangerous_deserialization=True)

# RAG Query Function
def rag_query(query):
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 6})
    model_name = "google/flan-t5-large"
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
    from langchain_community.llms import HuggingFacePipeline
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.2
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    # RAG retrieval
    docs = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])

    # Prompt template
    prompt = f"""
Use the given context to answer the question accurately.

Context:
{context}

Question:
{query}

Answer:
"""

    return llm.invoke(prompt)




if __name__ == "__main__":
    print("Building vector store...")
    build_vector_store()
    print("Vector store ready! Launch Streamlit using:  streamlit run ui.py")
