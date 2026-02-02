# Lexa

Lexa is a legal intelligence system powered by Retrieval-Augmented Generation (RAG). It allows users to query a database of legal cases and receive grounded answers with citations.

This README contains a Phase 1 functionality checklist, everything needed for Lexa to work properly.

---

## Lexa v1 Checklist

### 1. Data Ingestion System

- [x] Upload legal cases (PDF / text)
- [x] Extract text from documents
- [ ] Clean text (remove headers, footers, page numbers)
- [ ] Chunk text into smaller segments for AI processing
- [ ] Add metadata (case title, year, court, topics, case_id)

Turns raw legal documents into structured knowledge Lexa can understand.

---

### 2. Embeddings & Vector Storage

- [ ] Generate embeddings for each text chunk
- [ ] Store embeddings + metadata in MongoDB Vector Search
- [ ] Test retrieval by similarity search

Creates a semantic map of all legal knowledge for retrieval.

---

### 3. Retrieval Engine

- [ ] Embed user queries
- [ ] Search vector database for relevant chunks
- [ ] Optionally filter by metadata (court, year, topic)
- [ ] Return top-K relevant chunks

Finds the most relevant pieces of law to answer user queries.

---

### 4. RAG Orchestrator

- [ ] Assemble retrieved chunks into a prompt
- [ ] Define system instructions (grounded in sources, cite cases)
- [ ] Send prompt to LLM
- [ ] Parse response and return answer

Combines retrieved knowledge and AI reasoning to generate grounded answers.

---

### 5. API Layer

- [ ] Build `/ask` endpoint for user questions
- [ ] Build `/upload` endpoint for admin case ingestion
- [ ] Optional: `/cases` endpoint to list cases
- [ ] Test endpoints locally

Provides programmatic access to Lexa’s functionality.

---

### 6. (Optional) Frontend / UI

- [ ] Simple chat interface for user questions
- [ ] Display answers with cited cases
- [ ] Show retrieved chunks if needed
- [ ] Basic filters (year, court, topic)

Allows non-technical users to interact with Lexa easily.

---

### 7. Testing & Quality Assurance

- [ ] Test ingestion with multiple sample cases
- [ ] Test retrieval and query relevance
- [ ] Test LLM answers for grounding and citations
- [ ] Handle errors / missing data

Ensures Lexa works reliably and accurately.
