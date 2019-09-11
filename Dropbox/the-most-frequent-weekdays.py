from calendar import monthcalendar
from datetime import date
from collections import Counter
m = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def most_frequent_days(year: int):
    january = monthcalendar(year, 1)[0]
    december = monthcalendar(year, 12)[len(monthcalendar(year, 12)) - 1]
    s = list()
    for i in january:
        if i != 0:
            s.append(date(year, 1, i).strftime('%A'))
    for i in december:
        if i != 0:
            s.append(date(year, 12, i).strftime('%A'))
    return sorted([i[0] for i in Counter(s).most_common()
                   if i[1] == max(Counter(s).most_common(),
                                  key=lambda f: f[1])[1]], key=m.index)

if __name__ == '__main__':
    assert most_frequent_days(328) == ["Monday","Sunday"]
    assert most_frequent_days(1167) == ['Sunday']