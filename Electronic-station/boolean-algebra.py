OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction": return x&y
    if operation == "disjunction": return x|y
    if operation == "implication": return x<=y
    if operation == "exclusive":   return x^y
    if operation == "equivalence": return x==y
