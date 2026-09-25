chat_history = []


def add_message(
    role: str,
    content: str
):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )



def get_history():

    return chat_history