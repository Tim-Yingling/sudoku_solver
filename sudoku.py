# Constants
GRID_SIZE = 9
SUB_GRID_SIZE = 3


class Sudoku:
    def __init__(self) -> None:
        self.board = []

    def load_board(self, filename: str) -> None:
        with open(filename, 'r') as file:
            for line in file:
                row = [int(cell) for cell in line.strip().split(',')]
                self.board.append(row)

    def fill_board(self) -> None:
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell = int(input(f"Please input value for cell in row {i+1}, column {j+1} (0 for blanks): "))
                row.append(cell)
            self.board.append(row)

    def print_board(self) -> None:
        """
        Prints the current state of the Sudoku board to the console.
        """
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                # Print a vertical separator if we're at the start of a new sub-grid
                if (j > 0) and (j % SUB_GRID_SIZE == 0):
                    print("|", end=" ")
                # Print a blank space if the cell is empty, otherwise print the cell value
                if self.board[i][j] == 0:
                    print("_", end=" ")
                else:
                    print(self.board[i][j], end=" ")
                    
            # Print a horizontal separator if we're at the end of a sub-grid
            if (i < GRID_SIZE - 1) and ((i + 1) % SUB_GRID_SIZE == 0):
                print("\n----------------------")
            else:
                print()

    def start_solve(self) -> None:
        pass


game = Sudoku()
game.load_board("board.txt")
#game.fill_board()
game.print_board()