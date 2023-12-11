import os
from openai import OpenAI


def generate_text_with_emojis(sList_index, emoji_string):
    # Define the types of texts
    sList = ["tweet", "blog", "instagram caption", "e-mail"]

    # Extract the selected text type
    text_type = sList[sList_index]

    # Initialize the OpenAI client with your API key
    api_key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    # Create the completion request
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "You are a text assistant, that helps people write emails, blogs, captions, tweets."},
            {"role": "user",
             "content": "Compose a small " + text_type + " using " + emoji_string + " that makes context. Use them in the same order."}
        ]
    )

    # Return the generated text
    return completion.choices[0].message.content