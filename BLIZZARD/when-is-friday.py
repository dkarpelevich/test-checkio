from datetime import date

def friday(day):
    day = day.split('.')
    day_number = date(int(day[2]), int(day[1]), int(day[0])).weekday()
    return 4 - day_number if day_number <= 4 else 4 - day_number + 7

if __name__ == '__main__':
    print(friday('23.04.2018'))

    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
