import re

def checkio(words):
    word = re.split("[ ]+", words)
    count = 0
    for item in word:
        if not item.isdigit():
            count += 1
        elif item.isdigit():
            count = 0
        if count == 3:
            return True
    return False
