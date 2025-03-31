import tkinter as tk
import random

class CarCanvas(tk.Canvas):
    def __init__(self, master, car_color="blue", **kwargs):
        super().__init__(master, **kwargs)
        self.width = int(self["width"])
        self.car_x = 10
        self.car_y = int(self["heigh"]) // 2
        self.car_color = car_color
        self.car_body = self.create_rectangle(self.car_x, self.car_y - 10,
                                              self.car_x + 60, self.car_y + 10,
                                              fill=self.car_color)
        self.wheel1 = self.create_oval(self.car_x + 5, self.car_y + 10,
                                       self.car_x + 20, self.car_y + 25,
                                       fill="black")
        self.wheel2 = self.create_oval(self.car_x + 40, self.car_y + 10,
                                       self.car_x + 55, self.car_y + 25,
                                       fill="black")

    def move_car(self, dx):
        self.car_x += dx
        self.move(self.car_body, dx, 0)
        self.move(self.wheel1, dx, 0)
        self.move(self.wheel2, dx, 0)

    def reset(self):
        dx = 10 - self.car_x
        self.move_car(dx)

def race():
    global racing, winner
    if not racing:
        return

    for index, car in enumerate(car_canvases):
        dx = random.randint(1, 10)
        car.move_car(dx)
        if car.car_x + 60 >= car.width - 10:
            racing = False
            winner = index
            break

    if racing:
        root.after(100, race)
    else:
        winner_label.config(text=f"Победитель: автомобиль {winner + 1}")

def start_race():
    global racing, winner
    winner_label.config(text="")
    for car in car_canvases:
        car.reset()
    racing = True
    winner = None
    root.after(100, race)

root = tk.Tk()
root.title("Four Cars Race")

racing = True
winner = None

car_colors = ["red", "blue", "green", "yellow"]
car_canvases = []

for color in car_colors:
    cc = CarCanvas(root, car_color=color, width=600, height=80, bg="white")
    cc.pack(pady=5)
    car_canvases.append(cc)

start_button = tk.Button(root, text="Start Race", command=start_race)
start_button.pack(pady=10)

winner_label = tk.Label(root, text="", font=("Helvetica", 14))
winner_label.pack(pady=10)

root.mainloop()
