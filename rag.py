from rag_service import ask_question


if __name__ == "__main__":

    query = "What is the company's leave policy?"

    answer = ask_question(query)

    print("\nFinal Answer:\n")
    print(answer)