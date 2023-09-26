def long_repeat(line):

    number = 0
    counter = 0
    letter = ''
    if not line:
        return 0

    for iter in line:
        if letter != iter:
            letter = iter
            counter = 1
        else:
            counter += 1

        if number < counter:
            number = counter

    return number
