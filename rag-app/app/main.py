from fastapi import FastAPI
from app.services.pdf_service import extract_text_from_pdf


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