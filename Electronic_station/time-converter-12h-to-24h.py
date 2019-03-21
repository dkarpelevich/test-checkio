def time_converter(time):
    hours = time[:time.index(':')]
    hours = '0' + hours if len(hours) == 1 else hours

    minutes = time[time.index(':') + 1:time.index(' ')]
    second_part_of_day = True if time[time.index(' ') + 1:] == 'p.m.' else False

    if not second_part_of_day and hours == '12':
        return '00' + ':' + minutes
    if not second_part_of_day:
        return hours + ':' + minutes
    elif hours == '12':
        return hours + ':' + minutes
    else:
        return str(int(hours) + 12) + ':' + minutes

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:00 a.m.'))

    assert time_converter('12:00 a.m.') == '00:00'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")