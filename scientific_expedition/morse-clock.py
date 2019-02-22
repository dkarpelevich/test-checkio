def replace(time: str):
    return time.replace('0', '.').replace('1', '-')


def short_time_format(time: str):
    if len(time) == 1:
        return '0' + time
    else:
        return time


def format_time(format_time, time: str) -> str:
    return str(format_time).format((int(time)))


def checkio(time_string: str) -> str:
    hh, mm, ss = time_string.split(':')
    hh = short_time_format(hh)
    mm = short_time_format(mm)
    ss = short_time_format(ss)
    hh1 = format_time('{0:02b}', hh[0])
    hh2 = format_time('{0:04b}', hh[1])
    mm1 = format_time('{0:03b}', mm[0])
    mm2 = format_time('{0:04b}', mm[1])
    ss1 = format_time('{0:03b}', ss[0])
    ss2 = format_time('{0:04b}', ss[1])

    return str(replace(hh1) + ' ' + replace(hh2) + ' : ' +
               replace(mm1) + ' ' + replace(mm2) + ' : ' +
               replace(ss1) + ' ' + replace(ss2))


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
