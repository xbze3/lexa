from backend.app.utils.pdf_parser import parse_pdfs
from backend.app.core.chunking import chunker


def ingest():
    pdf_documents = parse_pdfs()
    chunks = chunker(pdf_documents)


if __name__ == "__main__":
    ingest()
