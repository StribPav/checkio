def sun_angle(time: str) -> Union[float, str]:
    hours = int(time[0:2])
    minutes = int(time[3:5])

    if hours == 18:
        check = 18 + minutes
    else:
        check = hours

    if 18 >= check >= 6:
        print((hours*60 + minutes - 360)*0.25)
        print(minutes - 360)
        return (hours*60 + minutes - 360)*0.25
    else:
        return "I don't see the sun!"
