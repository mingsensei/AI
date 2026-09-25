import ollama


def generate_answer(
    question,
    context
):

    prompt = f"""
Bạn là trợ lý AWS.

Chỉ trả lời dựa trên thông tin được cung cấp.

Context:

{context}


Question:

{question}


Answer:
"""


    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]