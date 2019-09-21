from string import ascii_lowercase

def to_decrypt(text, delta):
    text = ''.join(i for i in text if i.isalnum() or i == ' ')
    return text.translate(text.maketrans(ascii_lowercase, ascii_lowercase[delta:] + ascii_lowercase[:delta]))

if __name__ == '__main__':
    print("Example:")
    # print(to_decrypt('abc', 10))

    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")