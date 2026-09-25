import ollama


def generate_answer(
    question,
    context,
    sources,
    history
):


    messages = []


    messages.append(
        {
            "role": "system",
            "content": """
            Bạn là trợ lý AWS.
            Trả lời dựa trên context.
            Nếu không có thông tin trong context,
            hãy nói không biết.
            """
        }
    )


    messages.extend(
        history
    )


    messages.append(
        {
            "role": "user",
            "content": f"""

Context:

{context}


Sources:

{sources}


Question:

{question}

"""
        }
    )


    response = ollama.chat(
        model="qwen2.5:3b",
        messages=messages
    )


    return response["message"]["content"]