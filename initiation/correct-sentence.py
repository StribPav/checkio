def correct_sentence(text: str) -> str:
    text = text.replace('.','')
    text = text + '.'
    return text.capitalize()
