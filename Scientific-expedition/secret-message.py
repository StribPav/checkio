def find_message(text):
    """Find a secret message"""
    capital = str('')
    for i in text:
        if 'A' <= i <= 'Z':
            capital += i
    return capital
