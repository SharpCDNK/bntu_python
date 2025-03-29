import tkinter as tk

def move_line(event):
    global x, y
    if event.keysym == 'Up':
        canvas.create_line(x, y, x, y - step, fill='black')
        y -= step
    elif event.keysym == 'Down':
        canvas.create_line(x, y, x, y + step, fill='black')
        y += step
    elif event.keysym == 'Left':
        canvas.create_line(x, y, x - step, y, fill='black')
        x -= step
    elif event.keysym == 'Right':
        canvas.create_line(x, y, x + step, y, fill='black')
        x += step

window = tk.Tk()
window.title("Рисование линий с помощью клавиш со стрелками")


canvas_width = 400
canvas_height = 400
step = 20

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()


x = canvas_width // 2
y = canvas_height // 2


canvas.focus_set()
canvas.bind("<KeyPress-Up>", move_line)
canvas.bind("<KeyPress-Down>", move_line)
canvas.bind("<KeyPress-Left>", move_line)
canvas.bind("<KeyPress-Right>", move_line)


window.mainloop()
