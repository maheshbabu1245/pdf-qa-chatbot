# 📚 PDF Q&A Chatbot | Retrieval-Augmented Generation (RAG)

An AI-powered PDF Question Answering system that allows users to interact with their PDF documents using natural language. The application extracts document content, converts text into vector embeddings, stores them in ChromaDB, retrieves relevant information, and generates contextual answers using an LLM powered by Groq.

This project demonstrates the practical implementation of a Retrieval-Augmented Generation (RAG) pipeline for building document-based conversational AI applications.

## 🚀 Project Overview

Traditional document reading requires users to manually search through lengthy PDF files to find specific information.

This project simplifies that process by providing an intelligent document question-answering interface.

Users can upload or provide a PDF file, ask questions in natural language, and receive relevant answers generated using retrieved document context.

## ✨ Key Features

- **PDF Text Extraction:** Extracts textual information from PDF documents using PyPDF.
- **Text Processing:** Prepares extracted document content for retrieval.
- **Semantic Search:** Uses Sentence Transformers to generate vector embeddings.
- **Vector Database:** Stores and retrieves document embeddings using ChromaDB.
- **LLM Integration:** Uses Groq API to generate natural-language responses.
- **Context-Aware Q&A:** Combines retrieved document information with user queries to generate relevant answers.
- **Environment Security:** Uses environment variables to manage API credentials.
- **Scalable Architecture:** Provides a foundation for expanding into multi-document and enterprise knowledge-base applications.

## 🧠 RAG Architecture

The application follows a Retrieval-Augmented Generation workflow.

```text
             USER
               |
               v
        Upload PDF Document
               |
               v
         PDF Text Extraction
             (PyPDF)
               |
               v
          Text Processing
               |
               v
          Text Chunking
               |
               v
       Sentence Transformers
          (Embeddings)
               |
               v
          ChromaDB
        (Vector Storage)
               |
               |
       USER ASKS QUESTION
               |
               v
        Query Embedding
               |
               v
       Semantic Retrieval
          (ChromaDB)
               |
               v
      Retrieved Document Context
               |
               v
          Groq LLM API
               |
               v
       Contextual Answer
               |
               v
             USER
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| Groq | LLM inference API |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning utilities |
| Python-dotenv | Environment variable management |
| PyTorch | Deep learning framework |
| Transformers | Transformer model ecosystem |

## 📂 Project Structure

```text
pdf_QA_chatbot/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
├── README.md
│
└── chroma_db/
    └── Vector database files
```

*Note: Adjust the structure according to the actual files and folders in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd pdf_QA_chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your actual API key to GitHub.

### 6. Run the Application

```bash
python main.py
```

### 7. Provide Your PDF Path

When prompted, enter the complete PDF path, including the filename and extension.

Example:

```text
E:\ALL PDF\Complete SQL Tutorial.pdf
```

After successful extraction, start asking questions about your document.

## 🔍 How It Works

**1. Document Ingestion**

The system reads the provided PDF and extracts its textual content using PyPDF.

**2. Text Processing**

The extracted text is prepared and divided into smaller chunks to make document retrieval more efficient.

**3. Embedding Generation**

Sentence Transformers converts text chunks into numerical vector representations that capture semantic meaning.

**4. Vector Storage**

ChromaDB stores the generated embeddings and enables similarity-based retrieval.

**5. Query Processing**

When a user asks a question, the system converts the query into an embedding and searches for relevant document chunks.

**6. Contextual Response Generation**

The retrieved context is passed to the Groq-powered LLM, which generates a natural-language answer based on the available document information.

## 📸 Project Output

![pdf_QA_chatbot](Screenshot.png)

## 🔐 Security Considerations

- API credentials are stored using environment variables.
- `.env` should be excluded from version control.
- API keys should never be hardcoded or exposed in public repositories.
- Document access and data handling should be considered when extending the application.

## 🎯 Skills Demonstrated

This project demonstrates practical understanding of:

- Generative AI application development
- Large Language Model (LLM) integration
- Retrieval-Augmented Generation (RAG)
- PDF document processing
- Text preprocessing and chunking
- Semantic embeddings
- Vector databases
- Similarity search
- Context-aware question answering
- API integration
- Python application development
- Environment and dependency management

## 🚀 Future Improvements

- Support for multiple PDF documents.
- Conversational memory for follow-up questions.
- Streamlit-based interactive user interface.
- Source citations with page numbers.
- Hybrid search using BM25 and vector retrieval.
- Reranking using Cross-Encoder models.
- RAG evaluation using Precision, Recall, and Faithfulness.
- Deployment using Docker and cloud platforms.
- Authentication and document-level access control.

## 💼 Career Relevance

This project is designed to demonstrate practical GenAI engineering concepts relevant to entry-level roles such as:

- Generative AI Engineer
- Junior AI Engineer
- LLM Engineer Intern
- RAG Engineer Intern
- Python AI Developer

It demonstrates how document-based AI applications can be developed by combining embeddings, vector databases, retrieval pipelines, and LLM inference.

## 👨‍💻 Author

**Mahesh Kumar**

B.Tech – Artificial Intelligence and Data Science

**Technical Interests:** Generative AI | Large Language Models | RAG | NLP | Vector Databases | AI Agents

**GitHub:** https://github.com/maheshbabu1245

**LinkedIn:** https://www.linkedin.com/in/mahesh-kumar4

---

⭐ If you find this project useful, consider giving the repository a star!