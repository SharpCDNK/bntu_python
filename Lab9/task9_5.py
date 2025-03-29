import tkinter as tk
import random

def load_images():
    global x_image, o_image
    x_image = tk.PhotoImage(file="x.gif")
    o_image = tk.PhotoImage(file="o.gif")

window = tk.Tk()
window.title("Крестики-нолики")

load_images()

# Создаем сетку 3x3
for row in range(3):
    for col in range(3):
        rand_choice = random.randint(0, 1)
        image = x_image if rand_choice == 0 else o_image
        label = tk.Label(window, image=image)
        label.grid(row=row, column=col)

window.mainloop()
