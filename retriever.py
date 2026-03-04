import pandas as pd
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

print("Loading data...")

df = pd.read_csv("code_data.csv")

embeddings = np.load("embeddings.npy")

with open("code_index.pkl", "rb") as f:
    nn = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")


def search_code(query, k=3):

    query_embedding = model.encode([query])

    distances, indices = nn.kneighbors(query_embedding, n_neighbors=k)

    results = []

    for i in indices[0]:

        results.append({
            "language": df.iloc[i]["language"],
            "docstring": df.iloc[i]["docstring"],
            "code": df.iloc[i]["code"]
        })

    return results


if __name__ == "__main__":

    question = input("Ask coding question: ")

    results = search_code(question)

    for r in results:

        print("\nLanguage:", r["language"])
        print("Documentation:", r["docstring"])
        print("Code:\n", r["code"])