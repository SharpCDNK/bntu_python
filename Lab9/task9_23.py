import tkinter as tk

def change_color():
    color = color_var.get()
    label.config(bg=color)

def move_left():
    current_pos = label.place_info()
    x = int(current_pos['x']) - 10
    label.place(x=x, y=int(current_pos['y']))


def move_right():
    current_pos = label.place_info()
    x = int(current_pos['x']) + 10
    label.place(x=x, y=int(current_pos['y']))

window = tk.Tk()
window.geometry("600x600")
window.title("Кнопки и переключатели")


color_var = tk.StringVar(value="white")


label = tk.Label(window, text="Hello, World!", bg=color_var.get(), font=("Arial", 16))
label.place(x=225, y=150)


frame_colors = tk.Frame(window)
frame_colors.pack(pady=10)


colors = ["Red", "Yellow", "White", "Gray", "Green"]
for color in colors:
    tk.Radiobutton(frame_colors, text=color, variable=color_var, value=color, command=change_color).pack(side=tk.LEFT)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Left", command=move_left).pack(side=tk.LEFT, padx=5)

tk.Button(button_frame, text="Right", command=move_right).pack(side=tk.LEFT, padx=5)

window.mainloop()
