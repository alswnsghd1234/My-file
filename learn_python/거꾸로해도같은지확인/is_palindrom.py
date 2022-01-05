import string

def is_palindrome(text):
    text = ''.join(text.lower().split())
    for char in string.punctuation:
        text = text.replace(char, "")

    if text == "":
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
