#We have two edge cases here:
#if a cutting element cannot be found, then the sequence shouldn't be changed;
#if the sequence is empty, then it should remains empty.
#Input: List of integers (int).
#Output: List or other Iterable (tuple, iterator, generator ...) of integers (int).

from collections.abc import Iterable

def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    try:
        index = items.index(border)
        return items[:index + 1]
    except ValueError:
        return items

print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_after([], 0)) == []
assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]

print("The mission is done! Click 'Check Solution' to earn rewards!")
