class Matrix:

    def __init__(self, matrix_string):

        matrix = []

        for line in matrix_string.split("\n"):
            col_list = []
            for number in line.split():
                col_list.append(int(number))
            matrix.append(col_list)

        self.matrix = matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        ret = []
        for row in self.matrix:
            ret.append(row[index - 1])
        return ret
