from sudoku import Sudoku
from tkinter import *
import time

def load_board():
    """
    Loads the Sudoku board from the GUI entries.

    :return: A Sudoku object with the loaded board
    """

    # Create a list to hold the game board data
    game_board = []
    for entry in entries:
        row = []
        for cell in entry:
            data = cell.get()
            if data == '':
                row.append(0)
            else:
                row.append(int(data))
        game_board.append(row)
    return Sudoku(board=game_board, callback=update_grid)


def solve_sudoku():
    """
    Solves the Sudoku board and updates the GUI.

    :return: None
    """

    game = load_board()
    valid = game.start_solve()
    if valid:
        game.print_board()
    else:
        print('No solution to the board.')


def update_grid(row, col, val):
    """
    Updates the GUI with the solved Sudoku board.

    :param row: The row index to update
    :param col: The column index to update
    :param val: The value to update the cell with
    :return: None
    """

    entries[row][col].delete(0, END)
    entries[row][col].insert(0, val)

    # Add different color for 0 since it won't be part of the solution
    fg_color = 'blue' if val != 0 else 'darkred'

    entries[row][col].config(fg=fg_color)
    time.sleep(0.005)
    root.update_idletasks()


if __name__ == '__main__':
    # Create the main window
    root = Tk()
    root.title('Sudoku Solver')
    root.config(bg='darkgrey')

    # Set up entry boxes for sudoku board
    entries = []
    for i in range(9):
        row = []
        for j in range(9):
            empty_box = Entry(root, justify="center", width=2, font=('Arial', 24))
            
            # Determine the padding for cells to distinguish sub-grids
            pady = (7, 0) if i % 3 == 0 and i != 0 else (0, 0)
            padx = (7, 0) if j % 3 == 0 and j != 0 else (0, 0)
            empty_box.grid(row=i, column=j, padx=padx, pady=pady)

            row.append(empty_box)

        entries.append(row)

    # Create the solve button
    solve_button = Button(root, text="Solve", font=('Arial', 14), command=solve_sudoku)
    solve_button.grid(row=9, column=0, columnspan=9)

    # Start the main event loop
    root.mainloop()