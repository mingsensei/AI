from app.services.embedding_service import create_embeddings
from app.services.vector_service import search_similar
from app.services.llm_service import generate_answer
from app.services.memory_service import (
    add_message,
    get_history
)


def ask_rag(question: str):


    history = get_history()


    question_vector = create_embeddings(
        [question]
    )[0]


    results = search_similar(
        question_vector,
        top_k=3
    )


    documents = results["documents"][0]
    sources = results["metadatas"][0]

    context = "\n\n".join(
        documents
    )


    answer = generate_answer(
        question,
        context,
        sources,
        history
    )


    add_message(
        "user",
        question
    )


    add_message(
        "assistant",
        answer
    )


    return {
        "answer": answer,
        "history": history,
        "sources": sources
    }