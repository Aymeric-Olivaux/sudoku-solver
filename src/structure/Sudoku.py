

class Sudoku:
    core: list = []
    line_nb = 9
    column_nb = line_nb

    def __init__(self):
        for i in range(self.line_nb):
            self.core.append([])
        for i in range(self.line_nb):
            for j in range(self.column_nb):
                self.core[i].append(0)

    @staticmethod
    def build_with_entry():
        new_sudoku = Sudoku()
        nb = 0
        while nb < Sudoku.line_nb * Sudoku.column_nb:
            entry = input("Entry: ")
            if entry == "00":
                return new_sudoku
            list_entry = []
            list_entry[:0] = entry
            while len(entry) > 0:
                for i in range(Sudoku.line_nb):
                    for j in range(Sudoku.column_nb):
                        if len(list_entry) == 0:
                            break
                        if i * Sudoku.line_nb + j >= nb:
                            new_sudoku.core[i][j] = int(list_entry.pop(0))
                            nb += 1
                if len(list_entry) == 0:
                    break
            print(new_sudoku)
        return new_sudoku

    @staticmethod
    def build_with_string(string: str):
        new_sudoku = Sudoku()
        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                new_sudoku.core[i][j] = int(string[i * Sudoku.line_nb + j])
        Sudoku.sudoku = new_sudoku.core
        return new_sudoku

    def verifier(self):
        def verifier_line_i(new_self, i_element):
            if len(new_self.core[i_element]) != 9:
                new_self.core[i_element].pop(len(new_self.core[i_element]) - 1)
            line = new_self.core[i_element]
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
                column.append(new_self.core[element][j_element])
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

    def verifier_with_zero(self):
        def verifier_line_i_with_zero(new_self, i_element):
            line = new_self.core[i_element]
            line = line[:]
            if there_is_double(line):
                return False
            else:
                return True

        def verifier_column_j_with_zero(new_self, j_element):
            column = []
            for element in range(new_self.line_nb):
                column.append(new_self.core[element][j_element])
            column = column[:]
            if there_is_double(column):
                return False
            else:
                return True

        def verifier_square_i_j_with_zero(new_self, i_element, j_element):
            len_cube = int(Sudoku.line_nb / 3)
            origin_cube_line = int((i // len_cube) * len_cube)
            origin_cube_column = int((j // len_cube) * len_cube)
            l = []
            for i2 in range(origin_cube_line, origin_cube_line + len_cube):
                for j2 in range(origin_cube_column, origin_cube_column + len_cube):
                    l.append(new_self.core[i2][j2])
            if there_is_double(l):
                return False
            else:
                return True

        def there_is_double(l):
            founded = [0 for i in range(Sudoku.line_nb + 1)]
            for i in l:
                if i != 0:
                    founded[i] += 1

            for i in founded:
                if i > 1:
                    return True
            return False

        for i in range(self.line_nb):
            b = verifier_line_i_with_zero(self, i_element=i)
            if not b:
                return False
        for j in range(self.column_nb):
            b = verifier_column_j_with_zero(self, j_element=j)
            if not b:
                return False
        for i in range(self.line_nb):
            for j in range(self.column_nb):
                b = verifier_square_i_j_with_zero(self, i, j)
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
                string += str(self.core[i][j]) + " "
                if j == self.column_nb - 1:
                    string += "| "

            if i == self.line_nb - 1:
                string += "\n-------------------------"
            else:
                string += "\n"
        return string
