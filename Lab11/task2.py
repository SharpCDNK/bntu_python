import tkinter as tk
from tkinter import messagebox
import os
import sys
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Tic Tac Toe")

resample_filter = Image.Resampling.LANCZOS

x_image = Image.open("x.jpg").resize((50, 50), resample_filter)
o_image = Image.open("o.jpg").resize((50, 50), resample_filter)
empty_image = Image.open("empty.jpg").resize((50, 50), resample_filter)

x_img = ImageTk.PhotoImage(x_image, master=root)
o_img = ImageTk.PhotoImage(o_image, master=root)
empty_img = ImageTk.PhotoImage(empty_image, master=root)

current_player = "X"
cells = [[None for _ in range(3)] for _ in range(3)]

class Cell(tk.Label):
   def __init__(self, master, row, col, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.col = col
        self.token = ' '
        self.config(image=empty_img, borderwidth=2, relief="solid")
        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        global current_player
        if self.token != ' ':
            return

        self.token = current_player
        if current_player == "X":
            self.config(image=x_img)
        else:
            self.config(image=o_img)

        if check_winner(current_player):
            messagebox.showinfo("Игра окончена", f"Выиграл игрок {current_player}!")
            disable_all_cells()
        elif is_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            disable_all_cells()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner(player):
    for i in range(3):
        if cells[i][0].token == cells[i][1].token == cells[i][2].token == player:
            return True
    for j in range(3):
        if cells[0][j].token == cells[1][j].token == cells[2][j].token == player:
            return True
    if cells[0][0].token == cells[1][1].token == cells[2][2].token == player:
        return True
    if cells[0][2].token == cells[1][1].token == cells[2][0].token == player:
        return True
    return False

def is_draw():
    for row in cells:
        for cell in row:
            if cell.token == ' ':
                return False
    return True

def disable_all_cells():
    for row in cells:
        for cell in row:
            cell.unbind("<Button-1>")

def reset_game():
    global current_player
    current_player = "X"
    for row in cells:
        for cell in row:
            cell.token = ' '
            cell.config(image=empty_img)
            cell.bind("<Button-1>", cell.on_click)

board_frame = tk.Frame(root)
board_frame.pack(padx=10, pady=10)

for i in range(3):
    for j in range(3):
        cell = Cell(board_frame, i, j)
        cell.grid(row=i, column=j, padx=5, pady=5)
        cells[i][j] = cell

reset_button = tk.Button(root, text="Начать заново", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
