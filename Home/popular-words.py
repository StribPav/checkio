import re
def popular_words(text, words):
    return {word: text.lower().count(word) for word in words}
