import re


def check_red_words(text):
    text = text.lower()
    for i in re.findall('[^A-Za-z0-9 ]', text):
        text = text.replace(i, '')  # remove special symbols
    for i in text.split():
        if re.search(r"(h+e+l+p+)|(a+s+a+p+)|(u+r+g+e+n+t+)", i):
            return True


def is_stressful(text):
    if text.isupper() or text.endswith('!!!') or check_red_words(text):
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP!!!") == True, "Second"
    assert is_stressful("i need your H!E!L!P!") == True, "Second"
    assert is_stressful("i need urgen$t your a!!!saP") == True, "Second"
    assert is_stressful("i need your HH@@@HEEEEEEEEE$$$LLP") == True, "Second"
    print('Done! Go Check it!')
