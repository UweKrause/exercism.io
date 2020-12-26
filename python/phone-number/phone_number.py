class PhoneNumber:
    def __init__(self, input_dirty: str):

        input_clean = self.__validate_input(input_dirty)

        country_code, number = self.__separate_country_code_from_number(input_clean)

        if self.__check(country_code, number):
            self.number = number
            self.area_code = number[0:3]

    def __validate_input(self, number):
        cleaned_input = ''.join(filter(isdigit, number))

        if len(cleaned_input) != 10 and len(cleaned_input) != 11:
            raise ValueError("Invalid input length")

        return cleaned_input

    def __separate_country_code_from_number(self, input_clean: str):
        if len(input_clean) == 11:
            return input_clean[0], input_clean[1:11]
        else:
            return "1", input_clean

    def __check(self, country_code: str, number: str):
        if country_code != "1":
            raise ValueError("Invalid country code")

        if int(number[0]) < 2:
            raise ValueError("Invalid area code")

        if int(number[3]) < 2:
            raise ValueError("Invalid local number")

        return True  # redundant, but better for readability of constructor

    def pretty(self):
        # "(223)-456-7890"
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}'


def isdigit(string: str):
    return string.isdigit()
