from typing import List
from langchain_core.documents import Document
from tqdm import tqdm
import time
import requests

OLLAMA_BASE_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"

BATCH_SIZE = 16
TIMEOUT_SECONDS = 60
MAX_RETRIES = 3
BACKOFF_SECONDS = 2.0


def _embed_one(text: str) -> List[float]:

    last_err = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.post(
                f"{OLLAMA_BASE_URL}/api/embeddings",
                json={"model": EMBED_MODEL, "prompt": text},
                timeout=TIMEOUT_SECONDS,
            )
            r.raise_for_status()
            data = r.json()
            return data["embedding"]
        except Exception as e:
            last_err = e
            sleep_for = BACKOFF_SECONDS * attempt
            time.sleep(sleep_for)

    raise RuntimeError(f"Embedding failed after {MAX_RETRIES} retries: {last_err}")


def embed(documents: List[Document]):
    texts = [doc.page_content for doc in documents]
    vectors: List[list] = []

    num_batches = (len(texts) + BATCH_SIZE - 1) // BATCH_SIZE

    for b, i in enumerate(
        tqdm(
            range(0, len(texts), BATCH_SIZE),
            desc="Embedding batches",
            total=num_batches,
            unit="batch",
        ),
        start=1,
    ):
        batch = texts[i : i + BATCH_SIZE]

        with tqdm(
            total=len(batch),
            desc=f"Batch {b}/{num_batches}",
            unit="chunk",
            leave=False,
        ) as inner:
            for t in batch:
                vectors.append(_embed_one(t))
                inner.update(1)

    return vectors
