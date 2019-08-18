from typing import List

def checkio(number: str) -> List:
    number = ''.join(i for i in number if i.isalnum())[::-1]
    summa = 0
    for i in range(len(number)):
        point = ord(number[i]) - 48
        if i % 2 == 0:
            point = point*2
            summa += (point if point <= 9 else point // 10 + point % 10)
        else:
            summa += point
    return [str(0 if summa % 10 == 0 else 10 - (summa % 10)), summa]

if __name__ == '__main__':
    assert checkio("799 273 9871") == ["3", 67]
    assert checkio("139-MT") == ["8", 52]
    assert checkio("123") == ["0", 10]
    assert checkio("999_999") == ["6", 54]
    assert checkio("+61 820 9231 55") == ["3", 37]
    assert checkio("VQ/WEWF/NY/8U") == ["9", 201]