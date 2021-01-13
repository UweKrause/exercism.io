class Matrix:

    def __init__(self, matrix_string: str):
        self.matrix = [[int(number) for number in line.split()] for line in matrix_string.split("\n")]

    def row(self, index: int):
        return self.matrix[index - 1]

    def column(self, index: int):
        return [row[index - 1] for row in self.matrix]
