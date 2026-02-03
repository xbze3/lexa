from typing import List, Optional
from uuid import uuid4
from urllib.parse import urlparse
import chromadb
from langchain_core.documents import Document


def _parse_host_port(chroma_url: str):
    if "://" not in chroma_url:
        chroma_url = "http://" + chroma_url
    u = urlparse(chroma_url)
    return (u.hostname or "localhost", u.port or 8000)


def store(
    documents: List[Document],
    embeddings: List[list],
    *,
    collection_name: str = "lexa_cases",
    chroma_url: str = "http://localhost:8000",
    ids: Optional[List[str]] = None,
) -> int:
    if len(documents) != len(embeddings):
        raise ValueError(f"docs={len(documents)} embeddings={len(embeddings)} mismatch")

    dim0 = len(embeddings[0])
    print("STORE RECEIVED DIM:", dim0)

    host, port = _parse_host_port(chroma_url)
    client = chromadb.HttpClient(host=host, port=port)

    try:
        client.delete_collection(collection_name)
        print("Deleted collection:", collection_name)
    except Exception as e:
        print("Delete skipped:", e)

    col = client.get_or_create_collection(collection_name)

    if ids is None:
        ids = [str(uuid4()) for _ in documents]

    texts = [d.page_content for d in documents]
    metadatas = [d.metadata or {} for d in documents]

    col.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )

    return len(texts)
