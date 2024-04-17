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

    def is_valid_move(self, row, col, val) -> bool:
        # Check for value in given row
        if val in self.board[row]:
            return False
        # Check for value in given column
        elif val in [self.board[i][col] for i in range(GRID_SIZE)]:
            return False
        #Check for value in current sub-grid
        else:
            # Get top right coords of sub-grid using integer division
            start_row = (row // SUB_GRID_SIZE) * SUB_GRID_SIZE
            start_col = (col // SUB_GRID_SIZE) * SUB_GRID_SIZE

            for i in range(start_row, start_row + SUB_GRID_SIZE):
                for j in range(start_col, start_col + SUB_GRID_SIZE):
                    print(self.board[i][j])
                    # Return False if val is in sub-grid
                    if val == self.board[i][j]:
                        return False
            # Otherwise, return True
            return True
        
    def _solve(self, row, col, val) -> bool:
        return False
    
    def start_solve(self) -> bool:
        return False


game = Sudoku()
game.load_board("board.txt")
#game.fill_board()
if game.is_valid_move(5, 5, 7): print("Good!") 
else: print("No good!")
game.print_board()
