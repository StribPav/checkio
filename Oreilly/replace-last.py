def replace_last(line: list) -> Iterable:
    # your code here
    if len(line) == 0:
        return line
    elif len(line) == 1:
        return line
    else:
        last_element = line[-1]
        line = line[:-1]
        line.insert(0, last_element)
        return line


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
