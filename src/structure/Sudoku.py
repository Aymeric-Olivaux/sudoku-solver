class Sudoku:
    sudoku: list = []
    line_nb = 9
    column_nb = line_nb

    def __init__(self):
        for i in range(self.line_nb):
            self.sudoku.append([])
        for i in range(self.line_nb):
            for j in range(self.column_nb):
                self.sudoku[i].append(0)

    @staticmethod
    def build_with_entry():
        new_sudoku = Sudoku()
        b = False
        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                entry = "00"
                if not b:
                    entry = input("Entry: ")
                if entry == "00":
                    b = True
                if not b:
                    new_sudoku.sudoku[i] = entry
                else:
                    new_sudoku.sudoku[i] = 0
        return new_sudoku

    @staticmethod
    def build_with_string(string: str):
        new_sudoku = Sudoku()
        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                new_sudoku.sudoku[i][j] = int(string[i * Sudoku.line_nb + j])
        return new_sudoku

    def verifier(self):
        def verifier_line_i(new_self, i_element):
            line = new_self.sudoku[i_element]
            line = line[:]
            line.sort()
            expected = []
            for element in range(1, new_self.line_nb + 1):
                expected.append(element)
            if line != expected:
                return False
            else:
                return True

        def verifier_column_j(new_self, j_element):
            column = []
            for element in range(new_self.line_nb):
                column.append(new_self.sudoku[element][j_element])
            column = column[:]
            column.sort()
            expected = []
            for element in range(1, new_self.column_nb + 1):
                expected.append(element)
            if column != expected:
                return False
            else:
                return True

        for i in range(self.line_nb):
            b = verifier_line_i(self, i_element=i)
            if not b:
                return False
        for j in range(self.column_nb):
            b = verifier_column_j(self, j_element=j)
            if not b:
                return False
        return True

    def __str__(self):
        """
        Pretty printer
        :return: the string corresponding of the pretty printing of the sudoku
        """
        string: str = ""
        for i in range(self.line_nb):
            if i % 3 == 0:
                string += "-------------------------\n"
            for j in range(self.column_nb):
                if j % 3 == 0:
                    string += "| "
                string += str(self.sudoku[i][j]) + " "
                if j == self.column_nb - 1:
                    string += "| "

            if i == self.line_nb - 1:
                string += "\n-------------------------"
            else:
                string += "\n"
        return string
