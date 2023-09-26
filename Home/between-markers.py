def between_markers(text: str, begin: str, end: str) -> str:
    try:
        start = text.index(begin)+len(begin)
    except ValueError:
        start = None

    try:
        last = text.index(end)
    except ValueError:
        last = None

    return text[start:last]
