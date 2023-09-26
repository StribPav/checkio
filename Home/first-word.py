import re

def first_word(text: str) -> str:
    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.lstrip()
    return text.split(' ', 1)[0]
