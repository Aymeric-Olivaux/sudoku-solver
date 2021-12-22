from src.structure.Sudoku import Sudoku


class Hypothesis:

    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.core = []
        for i in range(Sudoku.line_nb):
            self.core.append([])
        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                self.core[i].append([])

        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                self.hypothesis_i_j(i, j)

    def hypothesis_i_j(self, i, j):
        if self.sudoku.sudoku[i][j] != 0:
            return
        for k in [i for i in range(1, Sudoku.line_nb + 1)]:
            a = Hypothesis.is_in_line_i(self.sudoku, i, k)
            b = Hypothesis.is_in_column_j(self.sudoku, j, k)
            c = Hypothesis.is_in_cube(self.sudoku, i, j, k)
            if not a and not b and not c:
                self.core[i][j].append(k)

    @staticmethod
    def is_in_line_i(sudoku, i, number):
        for j in range(Sudoku.column_nb):
            if sudoku.sudoku[i][j] == number:
                return True
        return False

    @staticmethod
    def is_in_column_j(sudoku, j, number):
        for i in range(Sudoku.line_nb):
            if sudoku.sudoku[i][j] == number:
                return True
        return False

    @staticmethod
    def is_in_cube(sudoku, i, j, numbers):
        len_cube = int(Sudoku.line_nb / 3)
        origin_cube_line = int((i // len_cube) * len_cube)
        origin_cube_column = int((j // len_cube) * len_cube)
        b = False
        for i2 in range(origin_cube_line, origin_cube_line + len_cube):
            for j2 in range(origin_cube_column, origin_cube_column + len_cube):
                if sudoku.sudoku[i2][j2] == numbers:
                    b = True
        return b

    def __str__(self):
        string: str = ""
        for i in range(Sudoku.line_nb):
            string += str(self.core[i]) + '\n'
        return string
