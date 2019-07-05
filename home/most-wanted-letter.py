from collections import Counter
from operator import itemgetter


def checkio(text: str) -> str:
    newstr = ''
    for i in text:
        if not i.isalpha():
            newstr += ''
        else:
            newstr += i
    list1 = Counter(newstr.lower()).most_common()
    for i in range(len(list1)):
        list1[i] = list(list1[i])
        list1[i][1] = list1[i][1] * (-1)
    result = sorted(list1, key=itemgetter(1, 0))
    return result[0][0]


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
    assert checkio("One") == "e", "All letter only once."
