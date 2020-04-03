def is_acceptable_password(password: str) -> bool:
    return len(password) > 6

if __name__ == '__main__':
    is_acceptable_password('short')
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True