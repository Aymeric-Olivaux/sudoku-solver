from src.structure.Sudoku import Sudoku

import unittest


class TestVerifier(unittest.TestCase):

    def test_verifier_true(self):
        string = "729364158" \
                 "615928374" \
                 "348715629" \
                 "493281765" \
                 "861597432" \
                 "257436981" \
                 "172843596" \
                 "936152847" \
                 "584679213"
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier(sudoku)
        print("b " + str(b))
        self.assertEqual(b, True)

    def test_verifier_false(self):
        string = "929364158" \
                 "615928374" \
                 "348715629" \
                 "493281765" \
                 "861597432" \
                 "257436981" \
                 "172843596" \
                 "936152847" \
                 "584679213"
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier(sudoku)
        self.assertEqual(b, False)

    def test_verifier_false2(self):
        string = "000000000"
        string = string * 9
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier(sudoku)
        self.assertEqual(b, False)

    def test_verifier_false3(self):
        string = "123456789"
        string = string * 9
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier(sudoku)
        self.assertEqual(b, False)

    def test_verifier_with_zero_True_1(self):
        string = "010000000"
        string += "0" * 9 * 8
        string = string
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier_with_zero(sudoku)
        self.assertEqual(True, b)

    def test_verifier_with_zero_True_2(self):
        string = "010000020"
        string += "0" * 9 * 8
        string = string

        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier_with_zero(sudoku)
        self.assertEqual(True, b)

    def test_verifier_with_zero_False_1(self):
        string = "0100000100"
        string += "0" * 9 * 8
        string = string
        sudoku = Sudoku.build_with_string(string)
        b = Sudoku.verifier_with_zero(sudoku)
        self.assertEqual(False, b)


if __name__ == '__main__':
    unittest.main()
