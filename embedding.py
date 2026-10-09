import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

text = "Employees are entitled to paid leave according to company policy."

def get_embedding(text):

    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )

    return result.embeddings[0].values




if __name__ == "__main__":

    text = "Employees are entitled to paid leave according to company policy."

    embedding = get_embedding(text)

    print("Embedding length:", len(embedding))
    print("First 10 values:", embedding[:10])

