def is_valid(isbn: str):
    # remove everything that is not a alphanumeric character
    # (keeping potentially wrong characters for now, will detect later)
    input_filtered_alphanumeric = ''.join(filter(isalnum, isbn))

    if len(input_filtered_alphanumeric) != 10:
        return False

    current_isbn_sum = 0  # accumulator

    """
    check the first 9 characters
    """
    current_factor = 10  # will be reduced, see isbn formula
    for i in range(0, 9):
        current_character = input_filtered_alphanumeric[i]
        if current_character.isdigit():
            current_isbn_sum += int(current_character) * current_factor
            current_factor -= 1
        else:
            return False

    """
    check last character (special rules apply)
    """
    current_character = input_filtered_alphanumeric[9]
    if current_character.isdigit():
        current_isbn_sum += int(current_character)
    elif current_character.lower() == "x":
        current_isbn_sum += 10
    else:
        return False

    return current_isbn_sum % 11 == 0


def isalnum(string: str):
    return string.isalnum()
