def checkio(first, second):
    new_str = []
    for st in first.split(','):
       if st in second.split(','):
          new_str.append(st)

    new_str.sort()

    return ','.join(new_str)
