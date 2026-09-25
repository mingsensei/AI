def split_text(
    text: str,
    source: str = "AWS.pdf",
    page: int = 1,
    chunk_size: int = 500,
    overlap: int = 50
):

    chunks = []

    start = 0

    index = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]


        chunks.append(
            {
                "text": chunk,
                "metadata": {
                    "source": source,
                    "page": page,
                    "chunk": index
                }
            }
        )


        index += 1

        start += chunk_size - overlap


    return chunks