import streamlit as st
from app import rag_query   # import your RAG function

st.set_page_config(page_title="RAG Search Assistant", layout="wide")

st.title("📘 RAG-Based Intelligent Search Assistant")
st.write("Ask questions based on the uploaded documents.")

# Input box
query = st.text_input("🔍 Enter your question:")

# When user clicks submit
if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a question!")
    else:
        with st.spinner("Searching..."):
            answer = rag_query(query)
        st.success("Answer:")
        st.write(answer)
