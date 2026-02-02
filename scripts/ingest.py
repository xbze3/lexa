from backend.app.utils.pdf_parser import parse_pdfs
from backend.app.utils.merger import merge_pages_by_source
from backend.app.core.chunking import chunker


def ingest():
    pdf_documents = parse_pdfs()
    merged_docments = merge_pages_by_source(pdf_documents)
    chunks = chunker(merged_docments)


if __name__ == "__main__":
    ingest()
