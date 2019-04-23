def correct_sentence(text: str) -> str:
    if text[len(text)-1] != '.':
        text = text + '.'
    return text[0].title() + text[1:]


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
