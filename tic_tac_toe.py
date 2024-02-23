#tic tac toe

import tkinter as tk
from tkinter import font

#class to represent the game board
class TicTacBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self.create_board_display()
        self.create_board_grid()
        
    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master = display_frame,
            text = "Ready?",
            font = font.Font(size=28, weight="bold"),
        )
        self.display.pack()
        
    #creating the grid of cells
    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, wieght=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master =grid_frame,
                    text = "",
                    font = font.Font(size=36, weight="bold"),
                    fg = "black",
                    width = 3,
                    height = 2,
                    highlight_background = "lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row = row,
                    column = col,
                    padx = 5,
                    pady = 5,
                    sticky = "nsew"
                )

#creating and calling the main loop of the game
def main():
    board = TicTacBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
