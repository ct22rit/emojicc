# List of emojis representing the first 127 ASCII characters in reverse
emojis = [
    "😀", "😃", "😄", "😁", "😆", "🥹", "😅", "😂", "🤣", "🥲", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
    "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
    "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😶‍🌫️", "😱",
    "😨", "😰", "😥", "😓", "🤗", "🤔", "🫣", "🤭", "🫢", "🫡", "🤫", "🫠", "🤥", "😶", "🫥", "😐", "🫤", "😑", "🫨", "😬",
    "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😮‍💨", "😵", "😵‍💫", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒",
    "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻",
    "😼", "😽", "🙀", "😿", "😾", "🫶", "🤲", "👐"
]

# Build the reverse ASCII to emoji mapping
reverse_ascii_to_emoji = {127 - index: emoji for index, emoji in enumerate(emojis)}


# Function to convert a string into its "reverse ASCII emoji" equivalent
def text_to_emoji(text):
    return ''.join(reverse_ascii_to_emoji[ord(char)] for char in text)


# Function to convert "reverse ASCII emoji" back to text
def emoji_to_text(emoji_text):
    emoji_to_reverse_ascii = {v: k for k, v in reverse_ascii_to_emoji.items()}
    # Decode emojis that are in the reverse mapping dictionary, insert space for others
    return ''.join(chr(emoji_to_reverse_ascii[char]) if char in emoji_to_reverse_ascii else '' for char in emoji_text)


# Sender's side
def sender():
    text = input("Enter your message to encode: ")
    encoded_message = text_to_emoji(text)
    print(f"Encoded message to send: {encoded_message}")
    return encoded_message


# Receiver's side
def receiver(encoded_message):
    text = emoji_to_text(encoded_message)
    print(f"Decoded message received: {text}")


text = input("Enter your message to decode: ")
receiver(text)