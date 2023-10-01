import re
import calendar
import re
import calendar
def date_time(time: str) -> str:
    #replace this for solution
    d, m, y, h, i = re.findall(r"[\w']+", time)
    converted_date = '{} {} {} year {} {} {} {}'.format(int(d), calendar.month_name[int(m)], y, int(h), ['hours', 'hour'][h=='01'], int(i), ['minutes', 'minute'][i=='01'])
    return converted_date
