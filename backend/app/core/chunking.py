from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunker(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=800,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(docs)

    return chunks
