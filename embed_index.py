import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import pickle

print("Loading dataset...")

df = pd.read_csv("code_dataset.csv")

texts = df["docstring"].astype(str).tolist()

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

embeddings = model.encode(texts, show_progress_bar=True)

embeddings = np.array(embeddings)

print("Creating search index...")

nn = NearestNeighbors(n_neighbors=5, metric="cosine")

nn.fit(embeddings)

with open("code_index.pkl", "wb") as f:
    pickle.dump(nn, f)

np.save("embeddings.npy", embeddings)

df.to_csv("code_data.csv", index=False)

print("Index created successfully!")