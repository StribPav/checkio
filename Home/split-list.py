def split_list(items: list) -> list:
    value_len = int(len(items) / 2)

    if len(items) == 0:
        new_list = [[], []]
    elif len(items) % 2 == 0:
        new_list = [items[:value_len], items[value_len:]]
    else:
        new_list = [items[:value_len + 1], items[value_len + 1:]]

    return new_list
