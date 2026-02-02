from typing import List
from backend.app.core.types.types import RetrievedChunk


def build_rag_prompt(question: str, sources: List[RetrievedChunk]) -> str:
    if not sources:
        return (
            "You are Lexa, a legal intelligence assistant.\n\n"
            f"User question:\n{question}\n\n"
            "No sources were retrieved. Say you do not have enough information."
        )

    blocks = []

    for s in sources:
        meta = s.metadata or {}

        title = meta.get("case_title") or meta.get("title") or ""
        year = meta.get("year") or ""
        court = meta.get("court") or ""
        page = meta.get("page")

        header_bits = [b for b in [title, str(year) if year else "", court] if b]
        header = " | ".join(header_bits)

        loc = f" (p{page})" if page is not None else ""
        header_line = f"{s.citation} {header}{loc}".strip()

        blocks.append(f"{header_line}\n{s.text}")

    sources_text = "\n\n---\n\n".join(blocks)

    return f"""You are Lexa, a legal intelligence assistant.
Answer the user using ONLY the sources provided below.
If the sources do not contain enough information, say so clearly.
Cite sources inline using the citation tags (example: [case_id:chunk_index]).

User question:
{question}

Sources:
{sources_text}
"""
