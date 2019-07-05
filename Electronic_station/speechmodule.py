from numbers_to_words_representation import all_numbers_representation as anr


if __name__ == '__main__':
    print(anr(1000))
    assert anr(12) == 'twelve', "1st example"
    assert anr(133) == 'one hundred thirty three', "2nd example"
    assert anr(12) == 'twelve', "3rd example"
    assert anr(101) == 'one hundred one', "4th example"
    assert anr(212) == 'two hundred twelve', "5th example"
    assert anr(40) == 'forty', "6th example"
    assert not anr(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
