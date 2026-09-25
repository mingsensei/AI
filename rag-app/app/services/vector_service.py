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

    ids = []

    for i in range(len(chunks)):
        ids.append(
            str(i)
        )


    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )


    return len(ids)
