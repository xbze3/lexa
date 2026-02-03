# Lexa

Local-First Legal Research & Intelligence Platform (RAG-based)

Lexa is a work-in-progress legal research and intelligence system built around Retrieval-Augmented Generation (RAG). My long term goal for the project is for it to become a full-fledged legal research platform, exposing a robust API and a frontend interface backed by a comprehensive legal document database.

At its current stage, Lexa focuses on:

- reliable document ingestion and normalization
- embeddings and semantic vector search
- grounded answer generation with citations
- modular, extensible backend architecture

Development is **temporarily paused** due to hardware constraints, but the foundation is stable and extensible.

---

## Project Vision

Lexa is designed to evolve into:

- A large-scale legal document repository (cases, statutes, judgments, reports)
- A high-quality legal search engine powered by hybrid retrieval (vector + keyword)
- A citation-aware legal reasoning assistant
- A backend API serving a modern web frontend
- A practical research tool for students, practitioners, and
  researchers

The current repository represents the core backend and RAG pipeline that future API and frontend layers will build upon.

---

## Current Capabilities

- PDF parsing and preprocessing
- Document merging and cleaning pipeline
- Intelligent document chunking
- Local embeddings using Ollama (`nomic-embed-text`)
- Vector storage and retrieval with ChromaDB
- Prompt construction with strict source grounding
- Local LLM-based answer generation (`mistral`)
- Inline source citations
- Modular ingestion → chunking → embedding → retrieval pipeline

---

## Architecture Overview

    PDF Documents
          ↓
    Parsing & Cleaning
          ↓
    Chunking
          ↓
    Embeddings (Ollama: nomic-embed-text)
          ↓
    ChromaDB Vector Store
          ↓
    Top-k Retrieval
          ↓
    Prompt Construction
          ↓
    LLM Answer Generation (Ollama: mistral)

---

## Technology Stack

#### Core Language & Runtime

- Python 3.11+

#### AI & RAG Stack

- **Ollama** - local LLM and embedding runtime
- **ChromaDB** - vector database for embeddings
- **LangChain (select utilities)** - document loading and
  orchestration

#### Data Processing

- **PyMuPDF**
- **Custom chunking and cleaning pipeline**
- **Dataclasses & typing** for structured document handling

#### Infrastructure & Tooling

- **Docker / Docker Compose**
- **Requests / tqdm** for networking and ingestion utilities

#### Planned / Future Stack

- **FastAPI** - backend API layer
- **PostgreSQL / SQLite** - metadata & structured storage
- **Next.js / React** - frontend interface
- **Hybrid retrieval (BM25 + embeddings)**
- **GPU inference (CUDA / ROCm)**

---

## Hardware Notes (Important)

Lexa is compute-intensive.

### Tested Environment

- CPU-only laptop (dual-core, low-power)
- \~8 GB RAM

### Observations

- Embeddings and retrieval perform well
- LLM generation (7B models) is **slow on CPU**
- Cold-start model loading can take 10+ minutes
- Long prompts may be truncated due to context limits

Because of this, active development is paused until access to more capable hardware (multi-core CPU or GPU).

The codebase remains functional, documented, and ready to resume.

---

## Running the Project (Backend Only)

### 1. Start services

```bash
docker compose up -d
```

### 2. Ingest documents

```bash
python -m scripts.ingest
```

### 3. Run interactive retrieval

```bash
python -m scripts.retrieve
```

---

## Dependencies & Setup

Lexa currently manages dependencies using a `requirements.txt` file. Environment variable configuration has not yet been implemented.

### Installing Dependencies

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
./venv/Scripts/activate  # On Mac: source venv/bin/activate
pip install -r requirements.txt
```

### requirements.txt

The `requirements.txt` file defines all core libraries required to run Lexa, including:

- PDF parsing and document processing libraries
- Vector database and embedding dependencies
- RAG pipeline utilities

---

## Development Status

✅ Core RAG pipeline implemented
✅ Ingestion, cleaning, and chunking pipeline working
✅ Embedding and retrieval validated
✅ Chroma schema and dimension handling stabilized
⏸️ API layer planned
⏸️ Frontend planned
⏸️ Scaling deferred pending hardware upgrade

---

## Roadmap (Planned)

- REST API for retrieval and generation (FastAPI)
- Authentication and multi-user support
- Frontend interface (Next.js)
- Dataset expansion and automated indexing pipeline
- Hybrid retrieval (vector + lexical search)
- Advanced citation handling and filtering
- Performance optimizations (GPU inference, batching, caching)
- Evaluation framework for retrieval and answer quality

---

## License

MIT License

---

## Author

Built by **Ezra Minty**
Early-stage legal tech research and experimentation project.

---

> Lexa is shared in its current state to document the design, architecture, and engineering decisions behind a local-first legal research system. Contributions, ideas, and future continuation are welcome.
