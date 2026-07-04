# AI Research Paper Intelligence System

An AI-powered web application that enables users to search research papers using **Semantic Search** and generate concise summaries using **Hugging Face Transformer models**. The project combines **Natural Language Processing (NLP)**, **Sentence Transformers**, **FAISS**, and **Streamlit** to create an intelligent research paper exploration platform.

---

## 🚀 Features

-  Semantic Search using Sentence Transformers
-  AI-powered Research Paper Summarization
-  Hugging Face Transformer Models (BART)
-  Fast Similarity Search with FAISS
-  NLP Text Preprocessing
-  Processed Research Paper Dataset
-  Interactive Streamlit Web Application
-  User-friendly Search Interface

---

##  Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- Streamlit
- Pandas
- NumPy
- NLTK
- Sentence Transformers
- Hugging Face Transformers
- FAISS
- PyTorch
- Scikit-learn



## 📌 NLP Techniques Used

- Text Cleaning
- Tokenization
- Stopword Removal
- Lemmatization
- Sentence Embeddings
- Semantic Search
- Vector Similarity Search
- Transformer-based Summarization

##  Project Structure

AI-Research-Paper-Intelligence-System/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── processed_research_paper.csv
│
├── notebooks/
│   └── Research_Paper_Intelligence_System.ipynb
│
├── images/
│
└── utils/

## Installation

### Clone the Repository
git clone https://github.com/gaurnaina123/AI-Research-Paper-Intelligence-System.git

### Move into the Project Folder
cd AI-Research-Paper-Intelligence-System


### Create a Virtual Environment (Optional)

Windows

python -m venv .venv
.venv\Scripts\activate


### Install Dependencies

pip install -r requirements.txt


##  Run the Application

By using this command:streamlit run app.py
The Streamlit application will open automatically in your web browser.



##  Workflow

1. Load the processed research paper dataset.
2. Generate sentence embeddings using Sentence Transformers.
3. Build a FAISS vector index.
4. Enter a search query.
5. Retrieve the most relevant research papers using semantic similarity.
6. Generate an AI-powered summary using the Hugging Face BART model.

---

##  Dataset

The application uses a processed CSV dataset containing research paper information.

Typical columns include:

- Title
- Abstract
- Authors
- Keywords
- Processed Text

# Future Enhancements

- Multi-document summarization
- RAG (Retrieval-Augmented Generation)
- LLM integration (Llama, Gemma, Mistral)
- Export summaries as PDF

# Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Semantic Search
- Vector Databases (FAISS)
- Sentence Embeddings
- Transformer Models
- Hugging Face Pipelines
- Streamlit Deployment
- AI-powered Information Retrieval



# Author:Naina Gaur

AI & Machine Learning Enthusiast

GitHub: https://github.com/gaurnaina123

