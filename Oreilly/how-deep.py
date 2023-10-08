def how_deep(structure: tuple) -> int:
    try:
        if not structure:
            return 1
        else:
            #return 1 + max(map(how_deep,structure))
            return 1 + max(how_deep(i) for i in structure)
    except:
        return 0

print("Example:")
print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
