from fastapi import FastAPI
from pydantic import BaseModel, Field

from rag_service import ask_question


app = FastAPI(
    title="Company Policy RAG API",
    description="AI-powered RAG application using Gemini and ChromaDB",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=1,
        description="Question about the company policy"
    )


class AnswerResponse(BaseModel):
    question: str
    answer: str


@app.get("/")
def root():
    return {
        "message": "Company Policy RAG API is running"
    }


@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):

    answer = ask_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }