import os
import json
import pandas as pd

BASE_PATH = "dataset"

languages = ["python", "java", "javascript", "php", "go", "ruby"]

data = []

def read_files(folder, lang):

    for file in os.listdir(folder):

        if file.endswith(".jsonl"):

            file_path = os.path.join(folder, file)

            with open(file_path, "r", encoding="utf-8") as f:

                for i, line in enumerate(f):

                    if i > 2000:   # limit for laptop
                        break

                    item = json.loads(line)

                    if item.get("code") and item.get("docstring"):

                        data.append({
                            "language": lang,
                            "docstring": item["docstring"],
                            "code": item["code"]
                        })


for lang in languages:

    path = os.path.join(BASE_PATH, lang, lang, "final", "jsonl")

    for split in ["train", "valid", "test"]:

        folder = os.path.join(path, split)

        if os.path.exists(folder):
            read_files(folder, lang)


df = pd.DataFrame(data)

print("Total samples:", len(df))

df.to_csv("code_dataset.csv", index=False)

print("Dataset saved successfully")