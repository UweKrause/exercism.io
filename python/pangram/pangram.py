import string


def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)

    for letter in sentence.lower():
        if letter in alphabet:
            alphabet.remove(letter)
            if len(alphabet) == 0:
                return True
    return False
