def time_converter(time):
    hours, minutes = time.split(':')
    time.splitlines()
    if 1 <= int(hours) <= 11:
        result = hours.lstrip('0') + ':' + minutes + ' a.m.'
    elif 13 <= int(hours) <= 23:
        result = str(int(hours) - 12) + ':' + minutes + ' p.m.'
    else:
        half = (' p.m.' if hours == '12' else ' a.m.')
        result = '12:' + minutes + half
    return result


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('00:30') == '12:30 a.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
