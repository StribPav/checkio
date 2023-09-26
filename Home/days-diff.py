from datetime import date
def days_diff(date1, date2):
    return abs((date(*date2) - date(*date1)).days)
