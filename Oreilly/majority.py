#We have a list of logic values (bool). Let's check if the majority of elements are True.
#Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount, function should return False.
#Input: A list of logic values (bool).
#Output: A logic value (bool).


def is_majority(items: list[bool]) -> bool:
    sum_bool = 0
    
    for i in items:
        if i == True:
            sum_bool += 1
        else:
            sum_bool -= 1

    return bool(sum_bool) if sum_bool > 0 else False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
