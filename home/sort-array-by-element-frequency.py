from collections import Counter


def frequency_sort(items: list) -> list:
    counts = Counter(items).most_common()
    inc_str: str = ''
    result_list: list = []
    for a, b in counts:
        inc_str += (str(a) + ' ') * int(b)
        try:
            a.isdigit()
            result_list += inc_str.split()
        except AttributeError:
            result_list += [int(i) for i in inc_str.split()]
        inc_str = ''
    print(result_list)
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))

    assert list(frequency_sort([4, 6, '2', '2', 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, '2', '2']
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")