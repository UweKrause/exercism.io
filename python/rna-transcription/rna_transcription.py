translation = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand):
    ret = ""
    for character in dna_strand:
        ret += translation[character]
    return ret
