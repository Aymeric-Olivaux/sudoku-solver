from src.structure.Sudoku import Sudoku
from src.structure.Hypothesis import Hypothesis


class Resolver:

    def run(self, sudoku: Sudoku, verbose = False):
        iteration = 0
        while iteration < 3000:
            sudoku = self.solver_lvl_2(sudoku)
            iteration += 1
            if sudoku.verifier():
                if verbose:
                    self.end(sudoku)
                return sudoku
        raise Exception("Timeout")

    @staticmethod
    def solver_lvl_1(sudoku: Sudoku):
        sudoku = Resolver.resolve_by_single_hypothesis(sudoku)
        return sudoku

    @staticmethod
    def solver_lvl_2(sudoku: Sudoku):
        sudoku = Resolver.resolve_by_solo_in_the_line(Resolver, sudoku)
        sudoku = Resolver.resolve_by_solo_in_the_column(Resolver, sudoku)
        #sudoku = Resolver.resolve_by_solo_in_the_square(Resolver, sudoku)
        sudoku = Resolver.resolve_by_single_hypothesis(sudoku)
        return sudoku
    @staticmethod
    def resolve_by_single_hypothesis(sudoku: Sudoku):
        hypothesis = Hypothesis(sudoku)
        for i in range(Sudoku.line_nb):
            for j in range(Sudoku.column_nb):
                if len(hypothesis.core[i][j]) == 1:
                    sudoku.core[i][j] = hypothesis.core[i][j][0]
        return sudoku

    @staticmethod
    def count_k_in_list_hypothesis(hypothesis_list, k):
        counter = 0
        position = False
        for i in range(len(hypothesis_list)):
            for j in hypothesis_list[i]:
                if k == j:
                    counter += 1
                    position = i
        return counter, position

    def resolve_by_solo_in_the_line(self, sudoku: Sudoku):
        hypothesis = Hypothesis(sudoku)
        for k in range(1, Sudoku.line_nb + 1):
            for i in range(len(hypothesis.core)):
                line = hypothesis.core[i]
                counter, position = self.count_k_in_list_hypothesis(line, k)
                if counter == 1:
                    sudoku.core[i][position] = k
        return sudoku

    def resolve_by_solo_in_the_column(self, sudoku: Sudoku):
        hypothesis = Hypothesis(sudoku)
        for k in range(1, Sudoku.line_nb + 1):
            for j in range(len(hypothesis.core)):
                column = []
                for i in range(len(hypothesis.core)):
                    column.append(hypothesis.core[i][j])
                counter, position = self.count_k_in_list_hypothesis(column, k)
                if counter == 1:
                    sudoku.core[position][j] = k
        return sudoku

    def resolve_by_solo_in_the_square(self, sudoku: Sudoku):
        hypothesis = Hypothesis(sudoku)
        for k in range(1, Sudoku.line_nb + 1):
            for i in range(0, Sudoku.line_nb / 3):
                i = i * 3 - 1
                for j in range(0, Sudoku.column_nb / 3):
                    j = j * 3 - 1
                    square = []
                    for i2 in range(i, i + 3):
                        for j2 in range(i, i + 3):
                            square.append(hypothesis.core[i2][j2])
                            counter, position = self.count_k_in_list_hypothesis(square, k)
                            if counter == 1:
                                sudoku.core[i + position // 3][j + position % 3] = k
        return sudoku

    @staticmethod
    def end(sudoku):
        print("Final Sudoku: ")
        print(sudoku)
