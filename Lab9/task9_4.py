import tkinter as tk

window = tk.Tk()
window.title("Шахматная доска")

cell_size = 50

for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = "white"
        else:
            color = "black"
        frame = tk.Frame(window, width=cell_size, height=cell_size, bg=color)
        frame.grid(row=row, column=col)

window.mainloop()
