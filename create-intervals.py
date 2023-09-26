def create_intervals(data):
    data = sorted(data)
    first = None
    second = 0
    list_tuple = []

    if not data:
        return []

    for i in data:
        #print(data)

        if first is None:
            first = i
        elif second != (i - 1):
            list_tuple.append((first, second))
            first = i

        second = i

    list_tuple.append((first, second))

    return list_tuple
