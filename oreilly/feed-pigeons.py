def checkio(food: int) -> int:
    minute = 0
    fed_pigeons = 0
    pigeons = 0
    while True:
        minute += 1
        old_pigeons = pigeons
        pigeons += minute
        if food < pigeons:
            remains_food = food - old_pigeons
            if remains_food > 0:
                fed_pigeons += remains_food
            break
        else:
            food -= pigeons
            fed_pigeons += minute
    return fed_pigeons

if __name__ == '__main__':
    assert checkio(1) == 1
    assert checkio(2) == 1
    assert checkio(5) == 3
    assert checkio(10) == 6