# Company Policy RAG System

An AI-powered Retrieval-Augmented Generation (RAG) application that answers questions from a company policy PDF using semantic search, vector embeddings, ChromaDB, and Google's Gemini model.

## Live Demo

- **Live API:** https://company-policy-rag-52nq.onrender.com
- **API Documentation (Swagger UI):** https://company-policy-rag-52nq.onrender.com/docs
- **GitHub Repository:** https://github.com/Salit03/genai-rag-project

## Project Overview

Traditional LLM applications can generate answers that are not supported by a specific company's documents. This project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a company policy document before generating an answer.

The application retrieves relevant document chunks from ChromaDB and provides them as context to the Gemini model. If the retrieved information does not sufficiently support an answer, the application can return a fallback response.

## Key Features

- PDF document loading and text extraction
- Text chunking using LangChain's RecursiveCharacterTextSplitter
- Text embeddings using Google's Gemini embedding model
- Persistent vector storage using ChromaDB
- Semantic similarity search for relevant document retrieval
- Context-based answer generation using Gemini
- REST API built with FastAPI
- Automatic API documentation using Swagger UI
- Input validation and handling of irrelevant questions
- Cloud deployment using Render

## Tech Stack

- **Language:** Python
- **LLM:** Google Gemini
- **Embeddings:** Gemini Embedding Model
- **RAG Framework Components:** LangChain Text Splitters
- **Vector Database:** ChromaDB
- **API Framework:** FastAPI
- **PDF Processing:** pypdf
- **Data Processing:** NumPy
- **Environment Management:** python-dotenv
- **API Testing:** Swagger UI and Postman
- **Version Control:** Git and GitHub
- **Deployment:** Render with Docker

## Architecture

```text
Company Policy PDF
        |
        v
PDF Loading and Text Extraction
        |
        v
Text Chunking
        |
        v
Generate Embeddings
        |
        v
Store Vectors in ChromaDB
        |
        v
      User Query
        |
        v
Generate Query Embedding
        |
        v
Semantic Similarity Search
        |
        v
Retrieve Relevant Chunks
        |
        v
Build Context and Prompt
        |
        v
Gemini LLM
        |
        v
Final Answer through FastAPI
```

## How It Works

1. **Document Loading:** Extract text from the company policy PDF using pypdf.
2. **Chunking:** Split the extracted text into smaller, manageable chunks using RecursiveCharacterTextSplitter.
3. **Embedding Generation:** Convert each document chunk into a numerical vector using Google's embedding model.
4. **Vector Storage:** Store the vectors, document chunks, and associated metadata in a persistent ChromaDB collection.
5. **Query Processing:** Convert the user's question into an embedding using the same embedding model.
6. **Retrieval:** Search ChromaDB for semantically relevant document chunks.
7. **Answer Generation:** Provide the retrieved context and user's question to Gemini to generate a grounded response.
8. **API Response:** Return the question and generated answer as a JSON response through FastAPI.

## API Usage

### Endpoint

`POST /ask`

### Request Body

```json
{
  "question": "How long must an employee work before they can request personal leave?"
}
```

### Example Response

```json
{
  "question": "How long must an employee work before they can request personal leave?",
  "answer": "An employee must have completed at least 12 months of service to request personal leave."
}
```

### Other Endpoints

- `GET /` — Checks whether the API is running.
- `POST /ask` — Answers questions using the RAG pipeline.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Salit03/genai-rag-project.git
cd genai-rag-project
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key. Never commit your API key to GitHub.

### 5. Start the application

```bash
uvicorn main:app --reload
```

Open the following URL in your browser:

`http://localhost:8000/docs`

Use Swagger UI to test the API.

## Project Structure

```text
genai-rag-project/
├── documents/          # Source PDF documents
├── chroma_db/          # Persistent ChromaDB vector index
├── gemini_client.py    # Gemini client and generation logic
├── document_loader.py  # PDF text extraction
├── chunking.py         # Text chunking
├── embedding.py        # Embedding generation
├── vector_store.py     # ChromaDB operations
├── ingest.py           # Document ingestion pipeline
├── retrieve.py         # Relevant chunk retrieval
├── similarity.py       # Cosine similarity implementation
├── rag.py              # RAG entry point
├── rag_service.py      # RAG orchestration
├── main.py             # FastAPI application
├── requirements.txt    # Python dependencies
├── .env                # Local environment variables
├── .gitignore
└── README.md
```

## Important Notes

- The ChromaDB index must be available to the application for retrieval to work.
- The Gemini API key must be configured as an environment variable.
- On Render, configure `GEMINI_API_KEY` in the service's environment settings.
- The free Render instance may spin down after inactivity, causing the first request to take longer.
- Avoid committing `.env`, virtual environments, or secret credentials to the repository.

## Future Improvements

- Add support for multiple PDF documents.
- Improve retrieval using metadata filtering and reranking.
- Add source citations to generated answers.
- Implement authentication and rate limiting.
- Add automated tests and structured error handling.
- Improve monitoring, logging, and deployment reliability.

## Learning Outcomes

- Understanding the end-to-end RAG pipeline
- Working with embedding models and vector databases
- Implementing semantic retrieval
- Integrating an LLM into a backend application
- Building REST APIs with FastAPI
- Deploying an AI application using Docker and Render

---

**Author:** Salit Kumar
