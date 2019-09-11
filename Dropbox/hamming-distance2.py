def checkio(first, second):
    first = bin(first)[2:]
    second = bin(second)[2:]
    diff = abs(len(first) - len(second))
    if len(first) > len(second):
        second = '0'*diff + second
    else:
        first = '0'*diff + first
    s = 0
    for i in range(len(first)):
        s += int(first[i]) ^ int(second[i])
    return s

if __name__ == '__main__':
    assert checkio(1, 2) == 2

