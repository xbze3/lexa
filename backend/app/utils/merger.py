from collections import defaultdict
from langchain_core.documents import Document


def merge_pages_by_source(docs):
    grouped = defaultdict(list)

    for doc in docs:
        grouped[doc.metadata["source"]].append(
            (doc.metadata.get("page", 0), doc.page_content)
        )

    merged_docs = []
    for source, pages in grouped.items():
        pages.sort(key=lambda x: x[0])
        full_text = "\n\n".join(text for _, text in pages)

        merged_docs.append(
            Document(
                page_content=full_text,
                metadata={"source": source},
            )
        )

    return merged_docs
