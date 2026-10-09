from retrieve import retrieve_documents
from gemini_client import generate


def ask_question(query, top_k=3):

    # 1. Retrieve relevant chunks
    results = retrieve_documents(
        query=query,
        top_k=top_k
    )

    # 2. Extract retrieved documents
    documents = results["documents"][0]

    # 3. Build context
    context = "\n\n".join(documents)

    # 4. Create RAG prompt
    prompt = f"""
You are a company policy assistant.

Answer the user's question using only the provided context.

If the answer is not available in the context, say:
"I don't have enough information in the provided company policy."

Context:
{context}

Question:
{query}
"""

    # 5. Generate answer
    answer = generate(prompt)

    return answer