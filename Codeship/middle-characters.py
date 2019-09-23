def middle(string):
    return string[len(string) // 2] if len(string) % 2 != 0 else string[len(string)//2-1:len(string)//2+1]

if __name__ == '__main__':
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
