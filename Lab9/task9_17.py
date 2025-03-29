import tkinter as tk

def move_car():
    global x, speed
    canvas.delete("all")
    canvas.create_image(x, y, image=car_image)
    x += speed
    if x > canvas_width:
        x = 0
    canvas.create_rectangle(0, canvas_height - 40, canvas_width, canvas_height, fill='gray')
    window.after(50, move_car)

def increase_speed(event):
    global speed
    speed += 100

def decrease_speed(event):
    global speed
    if speed > 2:
        speed -= 100


window = tk.Tk()
window.geometry("600x600")
window.title("Гоночный автомобиль")

canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

car_image = tk.PhotoImage(file='car.png')
car_width = car_image.width()
car_height = car_image.height()

x = -car_width
y = canvas_height - car_height - 40
speed = 10


window.bind("<Up>", increase_speed)
window.bind("<Down>", decrease_speed)

move_car()

window.mainloop()
