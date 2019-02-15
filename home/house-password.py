import re


def checkio(data: str) -> bool:
    if re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])", data) and len(data) >= 10:
        return True
    else:
        return False


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")