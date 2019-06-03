def checkio(marbles: str, step: int) -> float:
    i = 0
    denominator = len(marbles)
    list_of_marbles = [marbles]
    for i in range(step):
        for j in list_of_marbles:
            j.count('b')
            j.count('w')
    return 0.50


if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")