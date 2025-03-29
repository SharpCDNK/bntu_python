import tkinter as tk

def show_position(event,a):
    position = f"Позиция: ({event.x}, {event.y})"
    label.config(text=position)

def clear_position(event):
    label.config(text="")

window = tk.Tk()
window.geometry("600x600")
window.resizable(width=False, height=False)
window.title("Положение мыши при удержании")

label = tk.Label(window, text="Удерживайте кнопку мыши и перемещайте курсор.")
label.pack(pady=20)

window.bind("<B1-Motion>", show_position)
window.bind("<ButtonRelease-1>", clear_position)
window.mainloop()
