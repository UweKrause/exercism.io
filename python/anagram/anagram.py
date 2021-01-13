def find_anagrams(word: str, candidates: list[str]):
    equalized_word = equalize(word)

    return [candidate for candidate in candidates if
            anagram(candidate, equalized_word) and word.lower() != candidate.lower()]


def equalize(word: str):
    return sorted(list(word.lower()))


def anagram(candidate, word_order):
    return equalize(candidate) == word_order
