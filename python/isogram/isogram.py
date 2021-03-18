from string import ascii_lowercase


def is_isogram(string: str) -> bool:
    seen: [str] = []

    for x in string.lower():
        if x in ascii_lowercase:
            if x in seen:
                return False
            seen.append(x)

    return True
