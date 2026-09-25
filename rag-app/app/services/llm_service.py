import ollama



def generate_answer(
    question,
    context,
    history
):


    messages = []


    messages.append(
        {
            "role":"system",
            "content":
            """
            Bạn là trợ lý AWS.
            Trả lời dựa trên context.
            """
        }
    )


    messages.extend(
        history
    )


    messages.append(
        {
            "role":"user",
            "content":f"""
Context:

{context}


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