def slices(series, length):
    if length < 1 or len(series) < length:
        raise ValueError("Invalid Argument")

    ret = []

    start = 0
    stop = length
    for current in range(len(series) - length + 1):
        ret.append(series[start:stop])
        start += 1
        stop += 1

    return ret
