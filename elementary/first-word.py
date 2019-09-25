import re

def first_word(text: str) -> str:
    return re.search("[A-Za-z-']+", text).group(0)

def first_word_1(line):
    return ''.join(i if i.isalnum() or i == "'" else ' ' for i in line).split()[0]

if __name__ == '__main__':
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
