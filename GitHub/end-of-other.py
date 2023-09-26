def checkio(words):
    """
    You can iterate throught set.
    """
    for w in words:
        if w.endswith(tuple(x for x in words if x!=w)):
            return True
    return False
