from sudoku import Sudoku
from tkinter import *

def load_board():
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
    game = load_board()
    valid = game.start_solve()
    if valid:
        game.print_board()
    else:
        print('No solution to the board.')


def update_grid(row, col, val):
    entries[row][col].delete(0, END)
    entries[row][col].insert(0, val)
    entries[row][col].config(fg='green')


if __name__ == '__main__':
    root = Tk()
    root.title('Sudoku Solver')

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

    solve_button = Button(root, text="Solve", command=solve_sudoku)
    solve_button.grid(row=9, column=0, columnspan=9)

    root.mainloop()