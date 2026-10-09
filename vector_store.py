import chromadb


CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "company_policy"


client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=None
)


def add_documents(chunks, embeddings, metadatas):
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )



def search(query_embedding, top_k=3):
    print("ChromaDB path:", CHROMA_PATH)
    print("Collection:", COLLECTION_NAME)
    print("Total stored chunks:", collection.count())

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    print("Retrieved chunks:", len(results["documents"][0]))
    print("Retrieved content:", results["documents"][0])

    return results

