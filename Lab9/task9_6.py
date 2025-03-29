import tkinter as tk

def toggle_message(event):
    global message_index
    canvas.delete("all")
    canvas.create_text(150, 100, text=messages[message_index], font=("Arial", 16))
    message_index = 1 - message_index

window = tk.Tk()
window.title("Чередование сообщений")

messages = ["Programming is fun", "It is fun to program"]
message_index = 0

canvas = tk.Canvas(window, width=300, height=200, bg="white")
canvas.pack()

canvas.create_text(150, 100, text=messages[message_index], font=("Arial", 16))
message_index = 1 - message_index


canvas.bind("<Button-1>", toggle_message)

window.mainloop()
