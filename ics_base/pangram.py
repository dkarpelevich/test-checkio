import string


def check_pangram(text):
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if i not in text.lower():
            return False
    return True


if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert check_pangram("ABCDEF") == False
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')