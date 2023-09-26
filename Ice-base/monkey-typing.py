def count_words(text, words):
    counter = 0
    
    for word in words:
        #print(word)
        if word in text.lower():
            counter += 1
            #print(counter)

    if counter > 0:
        return counter

    return 0
