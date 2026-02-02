from backend.app.core.retrieval import retrieve
from backend.app.core.prompting import build_rag_prompt
from backend.app.core.llm import generate_answer


def retrieve(question: str, k: int = 5):
    sources = retrieve(question=question, k=k)
    prompt = build_rag_prompt(question, sources)
    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
    }


if __name__ == "__main__":
    q = input("Ask Lexa: ").strip()
    result = retrieve(q, k=5)

    print("\n--- ANSWER ---\n")
    print(result["answer"])

    print("\n--- SOURCES USED (top-k retrieved) ---\n")
    for s in result["sources"]:
        print(s.citation, s.metadata.get("case_title", ""), s.metadata.get("year", ""))
