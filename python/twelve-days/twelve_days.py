from num2words import num2words

stuff = {
    12: "Drummers Drumming",
    11: "Pipers Piping",
    10: "Lords-a-Leaping",
    9: "Ladies Dancing",
    8: "Maids-a-Milking",
    7: "Swans-a-Swimming",
    6: "Geese-a-Laying",
    5: "Gold Rings",
    4: "Calling Birds",
    3: "French Hens",
    2: "Turtle Doves",
    1: "a Partridge in a Pear Tree",
}


def validate_range(func):
    verse_min = 0
    verse_max = 12

    def inner(start_verse, end_verse):
        if start_verse <= verse_min or end_verse > verse_max:
            raise Exception("Not enough things")

        if end_verse < start_verse:
            raise Exception("Invalid order")

        return func(start_verse, end_verse)

    return inner


@validate_range
def recite(start_verse, end_verse):
    return [__build_verse(verse) for verse in range(start_verse, end_verse + 1)]


def __build_verse(verse):
    ret = f"On the {num2words(verse, 'ordinal')} day of Christmas my true love gave to me: "

    for item in range(verse, 1, -1):
        ret += f"{num2words(item)} {stuff[item]}, "

    if verse > 1:
        ret += "and "

    ret += f"{stuff[1]}."

    return ret
