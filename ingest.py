from document_loader import load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding import get_embedding
from vector_store import add_documents


PDF_PATH = "documents/company_policy.pdf"


def ingest_document():
    # 1. Load PDF
    text = load_pdf(PDF_PATH)

    # 2. Split document into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    print("Total chunks:", len(chunks))

    # 3. Generate embeddings
    embeddings = []

    for i, chunk in enumerate(chunks):
        print(f"Generating embedding {i + 1}/{len(chunks)}")

        embedding = get_embedding(chunk)
        embeddings.append(embedding)

    # 4. Create metadata
    metadatas = []

    for i in range(len(chunks)):
        metadatas.append({
            "source": "company_policy.pdf",
            "chunk_index": i
        })

    # 5. Store everything in ChromaDB
    add_documents(
        chunks=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("Documents successfully stored in ChromaDB.")


if __name__ == "__main__":
    ingest_document()