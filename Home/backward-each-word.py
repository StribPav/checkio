import re
def backward_string_by_word(text: str) -> str:

    reverse_words = ''

    lst = re.split('(\w+|\s)', text)

    for iterete in lst:
        reverse_words += iterete[::-1]

    return reverse_words
