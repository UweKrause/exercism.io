CodToPro = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}


def proteins(strand: str):
    codons = segment(strand)

    sequence = []
    for codon in codons:
        protein = CodToPro[codon]
        if protein == "STOP":
            return sequence
        else:
            sequence.append(protein)

    return sequence


def segment(instr: str, segment_len=3, segments=None):
    if segments is None:
        segments = []
    if len(instr) <= segment_len:
        segments.append(instr)
        return segments

    head = instr[0:segment_len]
    tail = instr[segment_len:len(instr)]

    segments.append(head)
    return segment(instr=tail, segment_len=segment_len, segments=segments)
