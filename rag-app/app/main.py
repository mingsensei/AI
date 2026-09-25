from fastapi import FastAPI
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import split_text

app = FastAPI()


@app.get("/")
def hello():
    return {
        "message": "RAG API"
    }


@app.get("/read-pdf")
def read_pdf():

    text = extract_text_from_pdf(
        "uploads/test.pdf"
    )

    return {
        "content": text
    }

@app.get("/chunk-pdf")
def chunk_pdf():

     text = extract_text_from_pdf(
         "uploads/test.pdf"
     )

     chunks = split_text(text)

     return {
         "total_chunks": len(chunks),
         "chunks": chunks[:3]
     }