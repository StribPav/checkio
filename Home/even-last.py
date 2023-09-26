def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if not array:
        return 0
    else:
        even_index = array[::2]
        sum_array = 0
        for item in even_index:
            sum_array += item
        return sum_array * array[-1]
