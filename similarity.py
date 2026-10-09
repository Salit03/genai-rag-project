import numpy as np

from embedding import get_embedding


def cosine_similarity(vector_a, vector_b):

    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    dot_product = np.dot(vector_a, vector_b)

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":

    text_1 = "Employees are entitled to paid leave according to company policy."

    text_2 = "Employees receive paid time off based on company rules."

    text_3 = "The company provides vehicles for approved business use."

    vector_1 = get_embedding(text_1)
    vector_2 = get_embedding(text_2)
    vector_3 = get_embedding(text_3)

    similarity_1_2 = cosine_similarity(
        vector_1,
        vector_2
    )

    similarity_1_3 = cosine_similarity(
        vector_1,
        vector_3
    )

    print("Text 1 vs Text 2:", similarity_1_2)

    print("Text 1 vs Text 3:", similarity_1_3)