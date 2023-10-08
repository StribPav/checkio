
def time_converter(time):
    # replace this for solution
    if time[-4:] == "a.m." and time[:-8] == "12":
        return "00" + time[-8:-5].strip()
    elif time[-4:] == "a.m.":
        return "0"+time[:-5].strip()
    elif time[-4:] == "p.m." and time[:2] == "12":
        return time[:-5].strip()
    else:
        return str(int(time[:-8]) + 12) + time[-8:-5].strip()

if __name__ == "__main__":
    print("Example:")
    print(time_converter("12:30 p.m."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("6:50 p.m.") == "18:50"
    assert time_converter("12:30 p.m.") == "12:30"
    assert time_converter("9:00 a.m.") == "09:00"
    assert time_converter("11:15 p.m.") == "23:15"
    print("Coding complete? Click 'Check' to earn cool rewards!")
