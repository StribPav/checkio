def checkio(number):
    string = str(number)
    s = 1
    for i in string.replace('0',''):
        t = int(i)
        s *= t

    return s
