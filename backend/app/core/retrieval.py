from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

import chromadb

from backend.app.core.embeddings import (
    _embed_one,
)
from backend.app.core.types.types import RetrievedChunk


CHROMA_URL = "http://localhost:8000"
COLLECTION_NAME = "lexa_cases"


def _parse_host_port(chroma_url: str):
    if "://" not in chroma_url:
        chroma_url = "http://" + chroma_url
    u = urlparse(chroma_url)
    return (u.hostname or "localhost", u.port or 8000)


def _citation_for(meta: Dict[str, Any], fallback_id: str):

    case_id = meta.get("case_id")
    chunk_index = meta.get("chunk_index")

    if case_id is not None and chunk_index is not None:
        return f"[{case_id}:{chunk_index}]"

    source = meta.get("source")
    page = meta.get("page")

    if source:
        filename = str(source).split("/")[-1].split("\\")[-1]
        if page is not None:
            return f"[{filename}:p{page}]"
        return f"[{filename}]"

    return f"[{fallback_id}]"


def retrieve(
    question: str,
    *,
    k: int = 5,
    chroma_url: str = CHROMA_URL,
    collection_name: str = COLLECTION_NAME,
) -> List[RetrievedChunk]:

    host, port = _parse_host_port(chroma_url)
    client = chromadb.HttpClient(host=host, port=port)
    collection = client.get_or_create_collection(collection_name)

    q_emb = _embed_one(question)

    res = collection.query(
        query_embeddings=[q_emb],
        n_results=k,
        include=["documents", "metadatas", "distances", "ids"],
    )

    docs = (res.get("documents") or [[]])[0]
    metas = (res.get("metadatas") or [[]])[0]
    dists = (res.get("distances") or [[]])[0]
    ids = (res.get("ids") or [[]])[0]

    out: List[RetrievedChunk] = []
    for text, meta, dist, _id in zip(docs, metas, dists, ids):
        meta = meta or {}
        citation = _citation_for(meta, fallback_id=_id)
        out.append(
            RetrievedChunk(
                text=text or "",
                metadata=meta,
                id=_id,
                distance=dist,
                citation=citation,
            )
        )

    return out
