from string import ascii_lowercase, ascii_uppercase

QUESTION: str = "Sure."
YELLING: str = "Whoa, chill out!"
YELLINGQUESTION: str = "Calm down, I know what I'm doing!"
NOTHING: str = "Fine. Be that way!"
ANYTHINGELSE: str = "Whatever."


def __strip_input(func):
    def inner(hey_bob: str) -> str:
        return func(hey_bob.strip())

    return inner


@__strip_input
def response(hey_bob: str) -> str:
    if len(hey_bob) == 0:
        return NOTHING

    is_yelling = __is_yeling(hey_bob)
    is_question = __is_question(hey_bob)

    if is_yelling and is_question:
        return YELLINGQUESTION

    if is_yelling:
        return YELLING

    if is_question:
        return QUESTION

    return ANYTHINGELSE


def __is_yeling(hey_bob: str) -> bool:
    is_no_lowercase: bool = not any(letter in ascii_lowercase for letter in hey_bob)
    is_all_uppercase: bool = any(letter in ascii_uppercase for letter in hey_bob)

    return is_no_lowercase and is_all_uppercase


def __is_question(hey_bob: str) -> bool:
    return hey_bob[-1] == "?"
