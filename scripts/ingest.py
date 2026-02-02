from backend.app.utils.pdf_parser import parse_pdfs


def ingest():
    pdf_documents = parse_pdfs()
    print(pdf_documents)


if __name__ == "__main__":
    ingest()
