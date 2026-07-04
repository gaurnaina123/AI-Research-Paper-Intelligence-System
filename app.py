import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load data


df = pd.read_csv(r"C:\Users\NAINA GAUR\processed_research_paper.csv")

# Models
model = SentenceTransformer("all-MiniLM-L6-v2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Embeddings (you can precompute later)
embeddings = model.encode(df["processed_text"].tolist())
embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Functions
def search(query):
    q = model.encode([query]).astype("float32")
    _, idx = index.search(q, 3)
    return df.iloc[idx[0]]

def summarize(text):
    return summarizer(text[:3000], max_length=120, min_length=40, do_sample=False)[0]["summary_text"]

# UI
st.title(" AI Research Paper Intelligence System")

option = st.selectbox("Choose Action", ["Search Papers", "Summarize Paper"])

if option == "Search Papers":

    query = st.text_input("Enter your query")

    if st.button("Search"):

        results = search(query)

        for i, row in results.iterrows():
            st.subheader(row["Section_Title"])
            st.write(row["Content"][:500])

elif option == "Summarize Paper":

    text = st.text_area("Paste text here")

    if st.button("Summarize"):

        st.write(summarize(text))