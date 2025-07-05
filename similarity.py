import os
import pickle
import gdown

def download_and_load_similarity():
    file_id = "10E2cedXTDUynyK0WqEUB86n2QP1Mvlf3"  # just the ID
    url = f"https://drive.google.com/uc?id={file_id}"
    filename = "similarity.pkl"

    if not os.path.exists(filename):
        print("📦 Downloading similarity.pkl ...")
        gdown.download(url, filename, quiet=False)
        print("✅ Download complete!")

    with open(filename, "rb") as f:
        similarity = pickle.load(f)
    return similarity
