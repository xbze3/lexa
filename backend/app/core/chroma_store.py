from __future__ import annotations

from typing import List, Optional
from uuid import uuid4

from tqdm import tqdm
from langchain_core.documents import Document
from langchain_chroma import Chroma

import chromadb


CHROMA_URL = "http://localhost:8000"
COLLECTION_NAME = "lexa_cases"

BATCH_SIZE = 64


def _batched(items: List, size: int):
    for i in range(0, len(items), size):
        yield items[i : i + size]


def store(
    documents: List[Document],
    embeddings: List[list],
    *,
    collection_name: str = COLLECTION_NAME,
    chroma_url: str = CHROMA_URL,
    ids: Optional[List[str]] = None,
) -> int:

    if len(documents) != len(embeddings):
        raise ValueError(
            f"documents and embeddings must be same length. "
            f"Got {len(documents)} docs, {len(embeddings)} embeddings."
        )

    if ids is not None and len(ids) != len(documents):
        raise ValueError(
            f"ids must be same length as documents. "
            f"Got {len(ids)} ids, {len(documents)} docs."
        )

    client = chromadb.HttpClient(
        host=_host_from_url(chroma_url), port=_port_from_url(chroma_url)
    )

    vectorstore = Chroma(
        client=client,
        collection_name=collection_name,
    )

    if ids is None:
        ids = [str(uuid4()) for _ in documents]

    texts = [d.page_content for d in documents]
    metadatas = [d.metadata or {} for d in documents]

    total = 0

    for doc_batch, emb_batch, id_batch, meta_batch in tqdm(
        zip(
            _batched(texts, BATCH_SIZE),
            _batched(embeddings, BATCH_SIZE),
            _batched(ids, BATCH_SIZE),
            _batched(metadatas, BATCH_SIZE),
        ),
        desc="Storing in Chroma",
        total=(len(texts) + BATCH_SIZE - 1) // BATCH_SIZE,
        unit="batch",
    ):
        vectorstore.add_texts(
            texts=list(doc_batch),
            embeddings=list(emb_batch),
            metadatas=list(meta_batch),
            ids=list(id_batch),
        )
        total += len(doc_batch)

    return total


def _host_from_url(url: str) -> str:
    url = url.replace("http://", "").replace("https://", "")
    return url.split(":")[0].strip("/")


def _port_from_url(url: str) -> int:
    url = url.replace("http://", "").replace("https://", "")
    parts = url.split(":")
    if len(parts) == 1:
        return 8000
    return int(parts[1].split("/")[0])
