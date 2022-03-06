from Resolver.Resolver import Resolver
from structure.Sudoku import Sudoku
from Generator.Generator import Generator
if __name__ == "__main__":
    sudoku = Sudoku.build_with_entry()
    resolver = Resolver
    sudoku = resolver.run(resolver, sudoku, verbose=True)
    #resolver = Resolver(sudoku)

