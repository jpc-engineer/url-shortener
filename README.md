# URL Shortener

A full-stack URL shortening service built from scratch.

This project features a decoupled architecture with a **FastAPI** backend handling RESTful API requests, a **SQLite** database for persistent storage, and a **Streamlit** frontend for a clean user interface.

## Features

- **FastAPI Backend:** High-performance REST API built with Python.
- **Strict Validation:** Uses Pydantic's `HttpUrl` to ensure only properly formatted web addresses are accepted.
- **Deterministic Hashing:** Generates 8-character short codes using truncated SHA-256 hashes of the long URL, ensuring idempotency (shortening the same URL twice yields the same code).
- **SQLite Persistence:** Stores URL mappings reliably using SQLAlchemy ORM.
- **302 Redirects:** Efficiently routes users to their target destinations using standard HTTP redirects.
- **Streamlit Frontend:** A clean, decoupled web UI that communicates with the backend via HTTP requests.
- **Error Handling:** Frontend detects offline backends and API validation errors, displaying user-friendly feedback instead of crashing.

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` (Python package manager)

### 1. Install Dependencies

Install the required Python libraries:

```bash
pip install fastapi uvicorn pydantic sqlalchemy streamlit requests
```

### 2. Start the backend
```bash
uvicorn app:app --reload
```
The backend will run on http://localhost:8000.

### 3. Start the frontend
```bash
streamlit run gui.py
```
A new browser tab will automatically open at http://localhost:8501.

## Testing via cURL
Create a short URL
```bash
curl -X POST http://localhost:8000/shorten \
-H "Content-Type: application/json" \
-d '{"url": "https://www.google.com"}'
```
Follow a redirect
```bash
curl -L http://localhost:8000/<YOUR_SHORT_CODE>
```
Delete a short URL
```bash
curl -X DELETE http://localhost:8000/<YOUR_SHORT_CODE>
```
