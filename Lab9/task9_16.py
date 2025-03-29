import tkinter as tk
import math

def animate_fan():
    global angle
    canvas.delete("all")
    x0, y0, x1, y1 = 50, 50, 250, 250
    canvas.create_oval(x0, y0, x1, y1, fill='white', outline='black')

    for i in range(4):
        start_angle = angle + i * 90
        canvas.create_arc(x0, y0, x1, y1, start=start_angle, extent=30, fill='black')

    angle += speed
    window.after(50, animate_fan)


angle = 0
speed = 50


window = tk.Tk()
window.title("Работающий вентилятор")

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

animate_fan()

window.mainloop()
