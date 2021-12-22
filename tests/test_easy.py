from src.structure.Sudoku import Sudoku
import unittest


class TestEasy(unittest.TestCase):

    def test_easy_1(self):
        string: str = "123456780"
        string = 9 * string
        new_sudoku = Sudoku.build_with_string(string)
        pass


if __name__ == '__main__':
    unittest.main()
