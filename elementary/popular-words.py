def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    d = dict()
    for i in words:
        d[i] = text.count(i)
    return d


if __name__ == '__main__':
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
