from string import ascii_lowercase

def to_encrypt(text, delta):
    return text.translate(text.maketrans(ascii_lowercase, ascii_lowercase[delta:] + ascii_lowercase[:delta]))

# def to_encrypt(text, delta):
#     alphas = "abcdefghijklmnopqrstuvwxyz"
#
#     cipher = [" " if c == " " else
#               alphas[(alphas.index(c) + delta) % 26]
#               for c in text]
#
#     return "".join(cipher)

# def to_encrypt(text, distance):
#     encrypted_text = str()
#     for letter in text:
#         if letter != ' ':
#             border_value = ascii_lowercase.index(letter) + distance
#             encrypted_text += ascii_lowercase[border_value - 26] \
#                 if border_value >= 0 else ascii_lowercase[border_value + 26]
#         else:
#             encrypted_text += ' '
#     return encrypted_text

if __name__ == '__main__':
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"