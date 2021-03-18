from string import ascii_lowercase, ascii_uppercase

QUESTION: str = "Sure."
YELLING: str = "Whoa, chill out!"
YELLINGQUESTION: str = "Calm down, I know what I'm doing!"
NOTHING: str = "Fine. Be that way!"
ANYTHINGELSE: str = "Whatever."


def response(hey_bob: str) -> str:
    strip: str = hey_bob.strip()

    if len(strip) == 0:
        return NOTHING

    yelling = True

    for l in strip:
        if l in ascii_lowercase:
            yelling = False
            break

    if yelling:
        yelling = any(x in ascii_uppercase for x in strip)

    question = strip[-1] == "?"

    if yelling and question:
        return YELLINGQUESTION

    if yelling:
        return YELLING

    if question:
        return QUESTION

    return ANYTHINGELSE
