import tkinter as tk

def draw_shape():
    canvas.delete("all")
    shape = shape_var.get()
    filled = filled_var.get()
    color = "blue"

    if shape == "rectangle":
        if filled:
            canvas.create_rectangle(50, 50, 250, 150, fill=color)
        else:
            canvas.create_rectangle(50, 50, 250, 150, outline=color)
    elif shape == "oval":
        if filled:
            canvas.create_oval(50, 50, 250, 150, fill=color)
        else:
            canvas.create_oval(50, 50, 250, 150, outline=color)

window = tk.Tk()
window.title("Выбор геометрической фигуры")

shape_var = tk.StringVar(value="rectangle")
filled_var = tk.BooleanVar()

control_frame = tk.Frame(window)
control_frame.pack(pady=10)

tk.Radiobutton(control_frame, text="Прямоугольник", variable=shape_var, value="rectangle", command=draw_shape).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(control_frame, text="Овал", variable=shape_var, value="oval", command=draw_shape).pack(side=tk.LEFT, padx=5)

tk.Checkbutton(control_frame, text="Заполненная", variable=filled_var, command=draw_shape).pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(window, width=300, height=200, bg="white")
canvas.pack()

draw_shape()

window.mainloop()
