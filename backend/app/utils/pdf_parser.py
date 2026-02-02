from pathlib import Path
from typing import List, Union

from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader


def parse_pdfs(data_dir: Union[str, Path] = None) -> List[Document]:
    """Load all PDFs under data_dir (recursively) into LangChain Documents."""

    if data_dir is None:

        base_dir = Path(__file__).resolve().parents[3]
        data_dir = base_dir / "data" / "sample"

    else:
        data_dir = Path(data_dir).expanduser().resolve()

    if not data_dir.exists():
        raise FileNotFoundError(f"PDF directory not found: {data_dir}")

    loader = DirectoryLoader(
        str(data_dir),
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader,
        show_progress=True,
        use_multithreading=True,
    )

    docs = loader.load()

    if not docs:
        raise ValueError(f"No PDFs found or no text extracted under: {data_dir}")

    return docs
