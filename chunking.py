from document_loader import load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

# def create_chunks(text,chunk_size =500,overlap=100):
#     chunks =[]
#     start =0
#     while start<len(text):
#         end = start+chunk_size
#         chunk = text[start:end]
#         chunks.append(chunk)
#         start = end -overlap
#     return chunks

## Testing / direct execution code
if __name__ == "__main__":
    text = load_pdf("documents/company_policy.pdf")
    spillter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
        
    )
    chunks = spillter.split_text(text)
    
    
     
     
    # chunks = create_chunks(text, chunk_size=500, overlap=100)
    
    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks):

        print("\n--- Chunk", i + 1, "---")
        print(chunk)
     
    