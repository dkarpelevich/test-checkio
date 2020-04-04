def backward_string_by_word_1(text: str) -> str:
    word = ''
    space = ''
    l = []
    text += ' '
    for i in text:
        if i != ' ':
            l.append(space)
            space = ''
            word += i
        else:
            l.append(word[::-1])
            word = ''
            space += i
    return ''.join(l)

import re
def backward_string_by_word_2(text: str) -> str:
    text1 = re.findall(r'\w+', text)
    for i in text1:
        text = text.replace(i, i[::-1])
    return text


def backward_string_by_word_3(text: str) -> str:
    ret = re.sub(r"\w+", lambda m: m.group()[::-1], text)
    return ret

def backward_string_by_word(text: str) -> str:
    return " ".join([i[::-1] for i in text.split(" ")])

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
