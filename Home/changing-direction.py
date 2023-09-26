def changing_direction(elements: list[int]) -> int:
    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')

    return len(dirs) - bool(dirs)
