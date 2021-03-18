color_codes = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: [str]) -> int:
    ret: str = ""
    for color in colors:
        ret += str(color_codes.index(color))

    return int(ret[:2])
