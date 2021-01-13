def distance(strand_a: str, strand_b: str):
    check(strand_a, strand_b)

    return len([(x, y) for x, y in zip(strand_a, strand_b) if x != y])


def check(a: str, b: str):
    if len(a) != len(b):
        raise ValueError("Comparables must have same size")
