def checkio(data):
    #replace this for solution
    #data = sorted(data)
    #listLen = len(data)
    #index = listLen // 2
    #if (listLen % 2):
    #    return data[index]
    #else:
    #    return (data[index] + data[index - 1])/2.0

    data.sort()
    #replace this for solution
    return data[len(data)//2] if len(data)%2 !=0 else (data[len(data)//2]+data[len(data)//2 -1])/2
