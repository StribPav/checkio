def missing_number(items: list[int]) -> int:
    list_steps = [0] * (len(items) - 1)
    items.sort()
    step_value = items[0]

    for indx in range(len(items) - 1):
        list_steps[indx] = items[indx + 1] - items[indx]

    list_steps.sort()
    step = list_steps[0]

    for indx in range(len(items) - 1):
        if (step_value + step) != items[indx + 1]:
           return step_value + step
        step_value = step_value + step

    return 0
