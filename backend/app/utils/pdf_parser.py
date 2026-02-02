from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyMuPDFLoader


def parse_pdf():

    BASE_DIR = Path(__file__).resolve().parents[3]
    DATA_DIR = BASE_DIR / "data" / "sample"

    pdf_dir_loader = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader,  # type: ignore
        show_progress=True,
    )

    pdf_documents = pdf_dir_loader.load()

    return pdf_documents
