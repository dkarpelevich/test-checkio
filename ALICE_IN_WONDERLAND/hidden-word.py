def horizontal_search(list_of_lines, word):
    for i in range(len(list_of_lines)):
        line = list_of_lines[i]
        if word in line:
            return [i + 1, line.index(word) + 1, i + 1, line.index(word) + len(word)]
    return False


def vertical_search(list_of_lines, word):
    max_len_line = max([len(i) for i in list_of_lines])
    vertical_list = ['' for _ in range(max_len_line)]
    for i in range(len(list_of_lines)):
        for j in range(len(list_of_lines[i])):
            vertical_list[j] += list_of_lines[i][j]
    h = horizontal_search(vertical_list, word)
    return [h[1], h[0], h[3], h[2]]


def checkio(text, word):
    text = text.replace(' ', '').lower()
    list_of_lines = text.splitlines()
    h_result = horizontal_search(list_of_lines, word)
    if not h_result:
        return vertical_search(list_of_lines, word)
    else:
        return h_result


if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
