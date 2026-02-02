from backend.app.utils.pdf_parser import parse_pdfs
from backend.app.utils.merger import merge_pages_by_source
from backend.app.core.chunking import chunker
from backend.app.core.embeddings import embed
from backend.app.core.chroma_store import store


def ingest():
    pdf_documents = parse_pdfs()
    merged_documents = merge_pages_by_source(pdf_documents)
    chunks = chunker(merged_documents)
    embeddings = embed(chunks)
    stored = store(documents=chunks, embeddings=embeddings)

    print(f"Vectors stored successfully: {stored} chunks stored")


if __name__ == "__main__":
    ingest()
