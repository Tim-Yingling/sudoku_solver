from sudoku import Sudoku
from tkinter import *

if __name__ == '__main__':
    game = Sudoku()
    game.load_board('board.txt')

    root = Tk()
    root.geometry('300x150')

    main_label = Label(root, text="Sudoku Solver")
    main_label.pack()

    solve_button = Button(root, text="Solve", command=game.start_solve)
    solve_button.pack()

    root.mainloop()

    game.print_board()