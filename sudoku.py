# Constants
GRID_SIZE = 9
SUB_GRID_SIZE = 3


class Sudoku:
    def __init__(self, board=[], callback=None) -> None:
        self.board = board
        self.callback = callback

    def load_board(self, filename: str) -> None:
        """
        Fills board with a given text file where cells are separated by commas and rows by lines
        
        :param filename: relative file path to the board
        """

        with open(filename, 'r') as file:
            for line in file:
                row = [int(cell) for cell in line.strip().split(',')]
                self.board.append(row)

    def fill_board(self) -> None:
        """Continuously asks the user to input board, cell by cell"""

        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell = int(input(f"Please input value for cell in row {i+1}, column {j+1} (0 for blanks): "))
                row.append(cell)
            self.board.append(row)

    def print_board(self) -> None:
        """Prints the current state of the board to the console"""

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
        """
        Checks if a move is valid given the current state of the board

        :param row: row index to try
        :param col: column index to try
        :param val: value to be placed
        :return: True if move is valid, otherwise False
        """

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
                    # Return False if val is in sub-grid
                    if val == self.board[i][j]:
                        return False
            # Otherwise, return True
            return True
        
    def _solve(self, row, col) -> bool:
        """
        Recursive function to solve the board

        :param row: row index to try a move
        :param col: column index to try a move
        :return: True if the rest of the board can be solved, otherwise False
        """

        # If we have reached past the last cell, then we've solved the board and can return True
        if (row == GRID_SIZE - 1 and col == GRID_SIZE):
            return True
        
        # If we reach over column limit, then reset and increment rows
        if col == GRID_SIZE:
            row += 1
            col = 0

        # If cell is already occupied by a number, then go to next cell
        if self.board[row][col] != 0:
            return self._solve(row, col + 1)
        
        # Try all possible values for given cell
        for x in range(1, 10): 
            # Check to see if x is a valid move
            if self.is_valid_move(row, col, x):
                # If x is valid, assume it belongs in the cell and update the board
                self.board[row][col] = x
                if self.callback:
                    self.callback(row, col, x)

                # Now we see if we can continue to solve the board. If we can, return True
                if self._solve(row, col + 1):
                    return True
                
                # If we cannot solve, our assumption is wrong and we must reset the cell
                self.board[row][col] = 0
                if self.callback:
                    self.callback(row, col, 0)

        return False


    def start_solve(self) -> bool:
        """
        Solve driver function

        :return: True if board is solved, otherwise False
        """

        if self._solve(0, 0):
            return True
        else:
            return False


if __name__ == '__main__':
    game = Sudoku()
    game.load_board("board.txt")
    #game.fill_board()
    if game.is_valid_move(5, 5, 7): print("Good!") 
    else: print("No good!")
    game.print_board()
    status = game.start_solve()
    print(status)
    game.print_board()
