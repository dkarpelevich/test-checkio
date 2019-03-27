def long_repeat(line):
    i = 0
    list_seq = []
    while i < len(line):
        count = 0
        for j in line[i:]:
            if j == line[i]:
                count += 1
            else:
                break
        i = i + count
        list_seq.append(count)
    try:
        return max(list_seq)
    except ValueError:
        return 0

if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('')  == 0, "Empty"
    print('"Run" is good. How is "Check"?')