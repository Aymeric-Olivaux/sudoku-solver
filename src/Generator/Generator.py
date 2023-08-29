from src.structure.Sudoku import Sudoku
from src.Resolver.Resolver import Resolver

class Generator:

    def __init__(self, lvl: int):
        self.lvl = lvl

    def generate_sudoku(self):
        sudoku = Sudoku()

        sudoku = Resolver.run(Resolver, sudoku)
        return sudoku
