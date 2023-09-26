def second_index(text: str, symbol: str):
    counter = 0
    ite = 0
    for i in text:
        if i == symbol:
            if ite == 1:
                return counter
            else:
                ite += 1
        counter += 1
    return None
