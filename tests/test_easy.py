from src.structure.Sudoku import Sudoku
from src.Resolver.Resolver import Resolver
import unittest


class TestEasy(unittest.TestCase):

    def test_easy_1(self):
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
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        print(sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_easy_2(self):
        string = "729364158" \
                 "615928374" \
                 "348715629" \
                 "493280765" \
                 "861597432" \
                 "257436981" \
                 "172843596" \
                 "936152847" \
                 "584679213"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        print(sudoku)
        self.assertEqual(True, sudoku.verifier())


    def test_easy_3(self):
        string = "729364158" \
                 "610928374" \
                 "348715629" \
                 "493280765" \
                 "861597432" \
                 "257436901" \
                 "172843596" \
                 "936152847" \
                 "584679213"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        print(sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_easy_4(self):
        string = "700364158" \
                 "615928374" \
                 "348715629" \
                 "493281765" \
                 "861597432" \
                 "257436981" \
                 "172843596" \
                 "936152847" \
                 "584679213"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        print(sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_easy_5(self):
        string = "700304008" \
                 "000908304" \
                 "000010009" \
                 "403001705" \
                 "061500030" \
                 "200030900" \
                 "102800506" \
                 "006102807" \
                 "080009010"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_easy_6(self):
        string = "604900800" \
                 "008764100" \
                 "000518642" \
                 "520180469" \
                 "780300050" \
                 "940050708" \
                 "897020310" \
                 "430691007" \
                 "105870924"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_easy_6_multiple(self):
        string = "604900800" \
                 "008764100" \
                 "000518642" \
                 "520180469" \
                 "780300050" \
                 "940050708" \
                 "897020310" \
                 "430691007" \
                 "105870924"
        string
        b = True
        for i in range(100):
            sudoku = Sudoku.build_with_string(string)
            resolver = Resolver
            sudoku = Resolver.run(resolver, sudoku, verbose=False)
            a =  sudoku.verifier()
            if not a:
                b = False
                break
        self.assertEqual(True, b)

    def test_easy_7(self):
        string = "658370924" \
                 "700002006" \
                 "012098000" \
                 "584109367" \
                 "026040510" \
                 "301086492" \
                 "840000673" \
                 "200034050" \
                 "030867240"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku, verbose=True)
        self.assertEqual(True, sudoku.verifier())

    def test_medium_easy_1(self):
        string = "700304008" \
                 "000908300" \
                 "000010009" \
                 "403001705" \
                 "061500030" \
                 "200030900" \
                 "102800506" \
                 "006102807" \
                 "080009010"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_medium_1(self):
        string = "000365410" \
                 "140009600" \
                 "000001008" \
                 "020013500" \
                 "009040800" \
                 "781596230" \
                 "004027185" \
                 "200104300" \
                 "000900700"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())

    def test_hard_1(self):
        string = "000006208" \
                 "000039164" \
                 "600042079" \
                 "000167893" \
                 "780000000" \
                 "391428057" \
                 "020900000" \
                 "138074900" \
                 "965200700"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())


    def test_expert_1(self):
        string = "050000000" \
                 "602810000" \
                 "000070100" \
                 "531060009" \
                 "000000000" \
                 "000020400" \
                 "000000007" \
                 "003040290" \
                 "000109830"
        sudoku = Sudoku.build_with_string(string)
        resolver = Resolver
        sudoku = Resolver.run(resolver, sudoku)
        self.assertEqual(True, sudoku.verifier())


if __name__ == '__main__':
    unittest.main()
