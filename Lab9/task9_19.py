import tkinter as tk

def move_circle(event):
    global x, y
    if event.keysym == 'Up':
        y -= step
    elif event.keysym == 'Down':
        y += step
    elif event.keysym == 'Left':
        x -= step
    elif event.keysym == 'Right':
        x += step
    draw_circle()

def draw_circle():
    canvas.delete("all")
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='blue')

window = tk.Tk()
window.title("Перемещение круга")

canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

x = canvas_width // 2
y = canvas_height // 2
radius = 20
step = 10

draw_circle()

canvas.focus_set()
canvas.bind("<KeyPress-Up>", move_circle)
canvas.bind("<KeyPress-Down>", move_circle)
canvas.bind("<KeyPress-Left>", move_circle)
canvas.bind("<KeyPress-Right>", move_circle)

window.mainloop()
