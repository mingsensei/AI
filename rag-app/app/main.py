from fastapi import FastAPI
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import split_text
from app.services.embedding_service import create_embeddings
from app.services.vector_service import save_embeddings
from app.services.vector_service import search_similar
from app.services.llm_service import generate_answer

from fastapi import Query

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
@app.get("/embedding-test")
def embedding_test():

    chunks = [
        "Amazon EC2 is a virtual server",
        "Amazon S3 is object storage"
    ]

    vectors = create_embeddings(
        chunks
    )

    return {
        "number_of_vectors": len(vectors),
        "dimension": len(vectors[0])
    }
@app.get("/pdf-embedding")
def pdf_embedding():

    text = extract_text_from_pdf(
        "uploads/test.pdf"
    )

    chunks = split_text(text)


    vectors = create_embeddings(
        chunks
    )


    return {
        "chunks": len(chunks),
        "vectors": len(vectors),
        "dimension": len(vectors[0])
    }
@app.get("/save-vector")
def save_vector():

    text = extract_text_from_pdf(
        "uploads/test.pdf"
    )


    chunks = split_text(text)


    vectors = create_embeddings(
        chunks
    )


    count = save_embeddings(
        chunks,
        vectors
    )


    return {
        "saved": count
    }

@app.get("/search")
def search(
    question: str = Query(...)
):

    question_vector = create_embeddings(
        [question]
    )[0]


    results = search_similar(
        question_vector
    )


    return results

@app.get("/chat")
def chat(
    question: str
):

    # 1. Embed question

    question_vector = create_embeddings(
        [question]
    )[0]


    # 2. Retrieve

    results = search_similar(
        question_vector,
        top_k=3
    )


    # 3. Get text

    documents = results["documents"][0]


    context = "\n\n".join(
        documents
    )


    # 4. Generate

    answer = generate_answer(
        question,
        context
    )


    return {
        "question": question,
        "answer": answer,
        "sources": documents
    }