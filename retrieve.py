from embedding import get_embedding
from vector_store import search


def retrieve_documents(query, top_k=3):

    # 1. Convert user query into embedding
    query_embedding = get_embedding(query)

    # 2. Search ChromaDB
    results = search(
        query_embedding=query_embedding,
        top_k=top_k
    )

    # 3. Return results
    return results


if __name__ == "__main__":

    query = "What is the company's leave policy?"

    results = retrieve_documents(query)

    print("\nRetrieved Documents:\n")

    for i, document in enumerate(results["documents"][0]):
        print(f"--- Result {i + 1} ---")
        print(document)
        print()