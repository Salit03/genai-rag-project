# Company Policy RAG System

An AI-powered Retrieval-Augmented Generation (RAG) application that answers questions from a company policy PDF using semantic search, vector embeddings, ChromaDB, and Google's Gemini model.

## Live Demo

- **Frontend Application:** https://company-policy-rag-frontend.onrender.com
- **Backend API:** https://company-policy-rag-52nq.onrender.com/
- **API Documentation (Swagger UI):** https://company-policy-rag-52nq.onrender.com/docs

## Source Code

- **Backend Repository:** https://github.com/Salit03/genai-rag-project
- **Frontend Repository:** https://github.com/Salit03/company-policy-rag-frontend

## Project Overview

Traditional LLM applications may generate answers that are not supported by a company's internal documents. This project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a company policy document before generating an answer.

The application converts document chunks into embeddings, stores them in ChromaDB, retrieves relevant chunks for a user's question, and provides the retrieved context to Google's Gemini model to generate a grounded response.

If the available policy context does not sufficiently support an answer, the application can return a fallback response.

## Key Features

- PDF document loading and text extraction using pypdf
- Text chunking using LangChain's RecursiveCharacterTextSplitter
- Text embeddings using Google's Gemini embedding model
- Vector storage and retrieval using ChromaDB
- Semantic similarity search for relevant document retrieval
- Context-based answer generation using Gemini
- REST API development using FastAPI
- Automatic API documentation using Swagger UI
- Request validation using Pydantic
- Fallback handling for insufficient policy information
- Cloud deployment using Render
- Interactive frontend built with Streamlit

## Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Large Language Model | Google Gemini |
| Embedding Model | Gemini Embedding Model |
| Text Chunking | LangChain Text Splitters |
| Vector Database | ChromaDB |
| Backend Framework | FastAPI |
| Frontend Framework | Streamlit |
| PDF Processing | pypdf |
| Numerical Processing | NumPy |
| Environment Configuration | python-dotenv |
| API Testing | Swagger UI, Postman |
| Version Control | Git, GitHub |
| Deployment | Render |

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
Generate Document Embeddings
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
Generate Final Answer
        |
        v
FastAPI Response
        |
        v
Streamlit Frontend
```

## How It Works

1. **Document Loading:** Extract text from the company policy PDF using pypdf.
2. **Text Chunking:** Split the extracted text into smaller chunks using RecursiveCharacterTextSplitter.
3. **Embedding Generation:** Convert document chunks into numerical vectors using Google's embedding model.
4. **Vector Storage:** Store document chunks, embeddings, and associated metadata in a ChromaDB collection.
5. **Query Processing:** Convert the user's question into an embedding using the same embedding model.
6. **Retrieval:** Search ChromaDB for document chunks that are semantically relevant to the question.
7. **Context Construction:** Combine the retrieved chunks with the user's question to construct the prompt.
8. **Answer Generation:** Send the prompt to Gemini to generate an answer grounded in the retrieved context.
9. **API Response:** Return the question and generated answer as JSON through FastAPI.
10. **Frontend Display:** Display the answer in the Streamlit application.

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

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| POST | `/ask` | Answers questions using the RAG pipeline |

Interactive API testing is available through the [Swagger UI](https://company-policy-rag-52nq.onrender.com/docs).

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Salit03/genai-rag-project.git
cd genai-rag-project
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key. Never commit API keys or other secret credentials to GitHub.

### 5. Prepare the Vector Database

Ensure the source PDF is available in the `documents/` directory and the ChromaDB collection has been populated.

If ingestion is required, run the ingestion script according to the project's current implementation:

```bash
python ingest.py
```

### 6. Start the Backend

```bash
uvicorn main:app --reload
```

Open the following URL to access the API documentation:

http://localhost:8000/docs

Use Swagger UI to test the API.

## Project Structure

```text
genai-rag-project/
├── documents/          # Source PDF documents
├── chroma_db/          # Local ChromaDB vector index
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
├── .env                # Local secrets; do not commit
├── .gitignore
└── README.md
```

## Deployment Notes

- The frontend and backend are deployed as separate Render services.
- The frontend sends questions to the backend's `/ask` endpoint.
- Free-tier services may spin down after inactivity, increasing the response time of the first request.
- Temporary `502 Bad Gateway` errors may occur if a service is unavailable or does not respond in time.
- The backend uses a local ChromaDB directory. Render's ephemeral filesystem can lose stored data after restarts, redeployments, or other lifecycle events.
- For reliable production use, configure persistent vector storage or a suitable external vector database and ensure the collection is available after deployment.
- Configure `GEMINI_API_KEY` in the backend service's environment settings on Render.

## Security Notes

- Never commit `.env`, API keys, or other secret credentials.
- Keep local virtual environments and generated files out of version control.
- Validate incoming API requests.
- Consider authentication, rate limiting, and monitoring before exposing the application to production users.

## Future Improvements

- Support multiple PDF uploads.
- Add metadata filtering and reranking to improve retrieval quality.
- Include source citations in generated answers.
- Implement authentication and rate limiting.
- Add automated tests and structured error handling.
- Improve monitoring, logging, and deployment reliability.
- Use persistent vector storage for reliable cloud deployments.

## Learning Outcomes

- Understanding the end-to-end RAG pipeline
- Working with embedding models and vector databases
- Implementing semantic retrieval
- Integrating an LLM into a backend application
- Building REST APIs using FastAPI
- Developing a frontend using Streamlit
- Deploying an AI application using Render

---

**Author:** Salit Kumar
