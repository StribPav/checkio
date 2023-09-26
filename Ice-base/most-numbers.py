def checkio(*args):
    if not args:
        return 0
    else:
        max_number = max(args)
        min_number = min(args)
        return max_number - min_number
