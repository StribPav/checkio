def verify_anagrams(first_word, second_word):

    if sorted(second_word.lower().replace(' ', '')) == sorted(first_word.lower().replace(' ', '')):
        return True

    return False
