import chromadb


client = chromadb.PersistentClient(
    path="./chroma"
)


collection = client.get_or_create_collection(
    name="documents"
)



def save_embeddings(
    chunks,
    embeddings
):

    documents = [
        chunk["text"]
        for chunk in chunks
    ]


    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]


    ids = [
        str(i)
        for i in range(len(chunks))
    ]


    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


    return len(ids)

def search_similar(
    query_embedding,
    top_k=3
):

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=top_k
    )


    return results

