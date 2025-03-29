import tkinter as tk
import math

def draw_fan():
    canvas.delete("all")
    x0, y0, x1, y1 = 50, 50, 250, 250
    canvas.create_oval(x0, y0, x1, y1, fill='white', outline='black')

    center_x = (x0 + x1) / 2
    center_y = (y0 + y1) / 2
    radius = (x1 - x0) / 2

    for i in range(4):
        angle = i * math.pi / 2
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        canvas.create_arc(x0, y0, x1, y1, start=angle * 180 / math.pi, extent=45, fill='black')


window = tk.Tk()
window.title("Неподвижный вентилятор")

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

draw_fan()

window.mainloop()
