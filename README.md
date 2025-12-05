📘 RAG-Based Intelligent Search Assistant

A Lightweight, Fast, and Fully Local Retrieval-Augmented Generation System

🌟 Overview

The RAG-Based Intelligent Search Assistant is a smart document-question answering system that allows users to ask natural language questions about any PDF and get accurate, context-grounded answers.

Instead of relying on cloud APIs or expensive models, the system uses:

FAISS for fast local vector search

Sentence-Transformer embeddings for semantic understanding

FLAN-T5 (HuggingFace) as a free, lightweight LLM

A clean Streamlit UI for seamless interaction

This creates a powerful mini “ChatGPT for your PDFs”—running completely on your local machine.

🎯 Key Features
🔍 Ask questions about any PDF

The system retrieves the most relevant text chunks from your documents and produces a grounded, context-aware answer.

⚡ Local & Free — No API Keys Required

Runs entirely on your system using HuggingFace models.
No OpenAI keys, billing issues, or rate limits.

🧠 RAG Architecture

Implements real Retrieval-Augmented Generation:

Document → Text → Chunks → Embeddings → FAISS Index → Retrieval → LLM Answer

🖥️ Interactive Streamlit UI

Beautiful interface where users can type questions and view answers instantly.

📄 PDF Support

Drop multiple PDFs into the data/ folder — the system will automatically process them.

🏗️ Architecture Diagram
             ┌──────────────────────┐
             │      PDF Files       │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │   Text Extraction    │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │   Chunking (RAG)     │
             └──────────┬───────────┘
                        │
                        ▼
            ┌─────────────────────────┐
            │ Sentence Embeddings      │
            └──────────┬──────────────┘
                        │
                        ▼
              ┌────────────────────┐
              │   FAISS Index      │
              └────────┬───────────┘
                       │
                       ▼
         ┌──────────────────────────────┐
         │ Relevant Chunk Retrieval     │
         └──────────┬───────────────────┘
                    │
                    ▼
       ┌──────────────────────────────┐
       │ FLAN-T5 LLM (HF Pipeline)   │
       └──────────┬───────────────────┘
                  │
                  ▼
          ┌──────────────────┐
          │   Final Answer    │
          └───────────────────┘

🚀 Getting Started
📦 1. Clone the repository
git clone <your-repo-url>
cd rag-search-assistant

📝 2. Install dependencies
pip install streamlit langchain langchain-community langchain-core \
            sentence-transformers faiss-cpu transformers accelerate \
            sentencepiece pypdf

📁 3. Add your PDFs

Place all your PDF files inside:

./data/

🧠 4. Build the vector store
python app.py


This will create a vector_index/ folder automatically.

🖥️ 5. Run the Streamlit app
python -m streamlit run ui.py


Your local RAG assistant will open in the browser.

🧪 Example Query

Question:
“Explain Generative AI based on the document.”

Answer:
(Generated using retrieved PDF content.)
A generative model is a type of AI system capable of producing new data such as text, images, audio…

🛠️ Tech Stack
Component	Technology
UI	Streamlit
LLM	HuggingFace Flan-T5
Embeddings	Sentence Transformers
Vector Search	FAISS
Framework	LangChain
Language	Python 3.12
📌 What Makes This Project Special?
✔ Fully Local, Privacy-Friendly

No data leaves your machine.

✔ Lightweight & Works on Normal Laptops

Flan-T5 is small, fast, and reliable.

✔ Clean Architecture

Shows real-world RAG implementation used in modern AI companies.

✔ Portfolio-Ready

Perfect addition for AI/ML internships and professional interviews.

📚 Use Cases

Summarize long documents

Question answering over PDFs

AI-driven knowledge search

Study assistant

AI-powered documentation explorer
