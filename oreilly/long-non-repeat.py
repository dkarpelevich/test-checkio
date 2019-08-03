def non_repeat(line: str) -> str:
    if line == '':
        return ''
    lines_list = []
    for j in range(len(line)):
        line_to_compare = line[j]
        for i in line[j+1:]:
            if i in line_to_compare:
                lines_list.append(line_to_compare)
                line_to_compare = i
            else:
                line_to_compare += i
        lines_list.append(line_to_compare)
    return max(lines_list, key=lambda x: len(x))

if __name__ == '__main__':
    assert non_repeat("") == ''
    assert non_repeat('abdjwawk') == 'abdjw'
    assert non_repeat('abcabcffab') == 'abcf'
