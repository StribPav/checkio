def checkio(text):
    import re
    list_sort = []
    letter_now = ''
    letter_amount = 0
    reg = re.compile('[^a-zA-Z]')
    string_lower = reg.sub('', text).lower()
    #print(string_lower)
    for i in string_lower:
        list_sort.append(i)
    #print(list_sort)
    list_sort.sort()

    for letter in list_sort:
        if letter_amount < list_sort.count(letter):
            letter_amount = list_sort.count(letter)
            letter_now = letter
    #def checkio(text):
    #    return max(ascii_lowercase, key=text.lower().count)

    #replace this for solution
    return letter_now
