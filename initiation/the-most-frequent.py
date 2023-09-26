def most_frequent(data):
    #a = ({word: data.count(word) for word in data})
    #return max(a, key=lambda key: a[key])
    return max(data, key=data.count)
