import math
from typing import List


def checkio(a: int, b: int, c: int) -> List[int]:
    if a+b <= c or a+c <= b or b+c <= a or a == 0 or b == 0 or c == 0:
        return [0, 0, 0]
    else:
        alpha = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c))))
        beta  = round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b))))
        gamma = 180 - alpha - beta
        return sorted([alpha, beta, gamma])


if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
