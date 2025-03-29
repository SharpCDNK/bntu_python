import tkinter as tk

def show_position(event):
    position = f"Позиция: ({event.x}, {event.y})"
    label.config(text=position)

window = tk.Tk()
window.title("Положение мыши")
window.geometry("600x600")

label = tk.Label(window, text="Нажмите кнопку мыши внутри окна.")
label.pack(pady=20)

window.bind("<Button-1>", show_position)

window.mainloop()
