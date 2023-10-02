import re
import calendar
import re
import calendar
def date_time(time: str) -> str:
    #replace this for solution
    d, m, y, h, i = re.findall(r"[\w']+", time)
    converted_date = '{} {} {} year {} {} {} {}'.format(int(d), calendar.month_name[int(m)], y, int(h), ['hours', 'hour'][h=='01'], int(i), ['minutes', 'minute'][i=='01'])
    return converted_date


def checkio(time):
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if dt.hour == 1 else 'hours'
    minute = 'minute' if dt.minute == 1 else 'minutes'
    return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')


def date_time(time: str) -> str:
    d = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    return d.strftime("{} %B %Y year {} hour{} {} minute{}").format(d.day, d.hour, "s" if d.hour != 1 else "", d.minute, "s" if d.minute != 1 else "")
