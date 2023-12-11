import random
import openaiff

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

noise_list = [
    "👐", "🙌", "👏", "🤝", "👍", "🤝", "👍", "👎", "👊", "✊", "🤛", "🤜", "🫷", "🫸", "🤞", "✌️", "🫰", "🤟", "🤘",
    "👌", "🤏", "🫳", "🫴", "👈", "👉", "👆", "👇", "☝️", "✋", "🖐️", "🖖", "👋", "🤙", "🫱", "🫲", "💪", "🦾", "🖕", "✍️",
    "🙏", "🫵", "🦶", "🦵", "🦿", "💄", "💋", "👄", "🫦", "🦷", "👅", "👂", "🦻", "👃", "👣", "👁️", "👀", "🫀", "🫁", "🧠",
    "🗣️", "👤", "👥", "🫂", "👶", "👧", "🧒", "👦", "👩", "🧑", "👨", "👩‍🦱", "🧑‍🦱", "👨‍🦱", "👩‍🦰", "🧑‍🦰", "👨‍🦰",
    "👱‍♀️", "👱", "👩‍🦰", "🧑‍🦰", "👨‍🦰", "👱‍♀️", "👱", "👱‍♂️", "👩‍🦳", "🧑‍🦳", "👨‍🦳", "👩‍🦲", "🧑‍🦲",
    "🧔‍♀️", "👨‍🦲", "👲", "👳‍♀️", "👳", "👳‍♂️", "🧕", "👮‍♀️", "👮", "👮‍♂️", "👷‍♀️", "👷", "👷‍♂️", "💂‍♀️",
    "💂", "💂‍♂️", "🕵️‍♀️", "🕵️", "🕵️‍♂️", "👩‍⚕️", "🧑‍⚕️", "👨‍⚕️", "👩‍🌾", "🧑‍🌾", "👨‍🌾", "👩‍🍳",
    "🧑‍🍳", "👨‍🍳", "👩‍🎓", "🧑‍🎓", "👨‍🎓", "👩‍🎤", "🧑‍🎤", "👨‍🎤", "👩‍🏫", "🧑‍🏫", "👨‍🏫", "👩‍🏭", "🧑‍🏭",
    "👨‍🏭", "👩‍💻", "🧑‍💻", "👨‍💻", "👩‍💼", "🧑‍💼", "👨‍💼", "👩‍🔧", "🧑‍🔧", "👨‍🔧", "👩‍🔬", "🧑‍🔬", "👨‍🔬",
    "👩‍🎨", "🧑‍🎨", "👨‍🎨", "👩‍🚒", "🧑‍🚒", "👨‍🚒", "👩‍✈️", "🧑‍✈️", "👨‍✈️", "👩‍🚀", "🧑‍🚀", "👨‍🚀"
]


# Function to add random noise to the encoded message
def add_noise(encoded_message, noise_list, noise_probability=0.1):
    noisy_message = ""
    for char in encoded_message:
        noisy_message += char
        # Decide whether to add noise after each character based on the noise_probability
        if random.random() < noise_probability:
            noisy_message += random.choice(noise_list)
    return noisy_message


# Build the reverse ASCII to emoji mapping
reverse_ascii_to_emoji = {127 - index: emoji for index, emoji in enumerate(emojis)}


# Function to convert a string into its "reverse ASCII emoji" equivalent
def text_to_emoji(text):
    return ''.join(reverse_ascii_to_emoji[ord(char)] for char in text)


# Function to convert "reverse ASCII emoji" back to text
def emoji_to_text(emoji_text):
    emoji_to_reverse_ascii = {v: k for k, v in reverse_ascii_to_emoji.items()}
    return ''.join(chr(emoji_to_reverse_ascii[char]) for char in emoji_text)


# Sender's side
def sender():
    text = input("Enter your message to encode: ")
    encoded_message = text_to_emoji(text)
    final_message = add_noise(encoded_message, noise_list, 0.0)
    print(f"Encoded message to send: {final_message}")
    AIuse(final_message)
    return encoded_message


def AIuse(final_message):
    index = int(input("What would you like to generate?\n 1.Tweet\n 2.Blog \n 3.Instagram Caption \n 4. E-mail \n:"))
    print(openaiff.generate_text_with_emojis(index-1, final_message))



# Receiver's side
def receiver(encoded_message):
    text = emoji_to_text(encoded_message)
    print(f"Decoded message received: {text}")


sender()
