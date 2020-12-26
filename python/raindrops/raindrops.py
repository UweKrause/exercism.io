"""
has 3 as a factor, add 'Pling' to the result.
has 5 as a factor, add 'Plang' to the result.
has 7 as a factor, add 'Plong' to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
"""

"""
28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
34 is not factored by 3, 5, or 7, so the result would be "34".
"""


def convert(number):
    ret = ""
    if number % 3 == 0:
        ret += "Pling"
    if number % 5 == 0:
        ret += "Plang"
    if number % 7 == 0:
        ret += "Plong"

    if len(ret) != 0:
        return ret
    else:
        return str(number)
