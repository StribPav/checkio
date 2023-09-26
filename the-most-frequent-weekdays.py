import datetime
def most_frequent_days(year):
    first_day = datetime.date(year, 1, 1)
    last_day = datetime.date(year, 12, 31)
    names_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    count_days = [0] * 7   #[monday_count_days, tuesday_count_days, ...]
    list_days = []

    # count first week
    for counter in range(first_day.weekday(), 7):
        count_days[counter] += 1

    # count last week
    for counter in range(0, last_day.weekday() + 1):
        count_days[counter] += 1

    max_days = max(count_days)
    
    for index, sum_days in enumerate(count_days):
        if sum_days == max_days:
            list_days.append(names_days[index])

    return list_days
