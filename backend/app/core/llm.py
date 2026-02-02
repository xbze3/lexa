import os
import requests

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
ANSWER_MODEL = os.getenv("OLLAMA_ANSWER_MODEL", "mistral")

TIMEOUT_SECONDS = 600


def generate_answer(prompt: str) -> str:

    r = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": ANSWER_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=TIMEOUT_SECONDS,
    )
    r.raise_for_status()
    return (r.json().get("response") or "").strip()
