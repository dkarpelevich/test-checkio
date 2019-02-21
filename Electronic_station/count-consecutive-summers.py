def count_consecutive_summers(num):
    num_middle = num // 2
    summ = 0
    result = 1
    for i in range(1, num_middle + 1):
        for j in range(i, num_middle + 2):
            summ += j
            if summ == num:
                result += 1
                break
            elif summ > num:
                break
        summ = 0
    return result


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(1))

    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")