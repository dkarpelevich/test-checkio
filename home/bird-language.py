consonants = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouy"

def translate(phrase):
    for i in range(len(phrase)):
        if i == len(phrase):
            break
        if phrase[i] in consonants:
            phrase = phrase[:i+1] + phrase[i+2:]
    for i in VOWELS:
        if i*3 in phrase:
            phrase = phrase.replace(i*3, i)
    return phrase

if __name__ == '__main__':
    print("Example:")
    # print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
