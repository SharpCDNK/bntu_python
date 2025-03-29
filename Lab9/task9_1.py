import tkinter as tk

class BallPanel:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack()
        self.ball_size = 20
        self.ball = self.canvas.create_oval(140, 140, 160, 160, fill='blue')

    def move_ball(self, dx, dy):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        if x1 + dx < 0:
            dx = 0
        if y1 + dy < 0:
            dy = 0
        if x2 + dx > self.canvas.winfo_width():
            dx = 0
        if y2 + dy > self.canvas.winfo_height():
            dy = 0
        self.canvas.move(self.ball, dx, dy)
        print(x1, ' ', y1, ' ', x2, ' ', y2, ' ', self.canvas.winfo_width(), ' ', self.canvas.winfo_height())

def create_buttons(frame, panel):
    tk.Button(frame, text='Left', command=lambda: panel.move_ball(-10, 0)).grid(row=1, column=0)
    tk.Button(frame, text='Right', command=lambda: panel.move_ball(10, 0)).grid(row=1, column=2)
    tk.Button(frame, text='Up', command=lambda: panel.move_ball(0, -10)).grid(row=0, column=1)
    tk.Button(frame, text='Down', command=lambda: panel.move_ball(0, 10)).grid(row=2, column=1)

def main():
    root = tk.Tk()
    root.title("The Ball")
    panel = BallPanel(root)
    button_frame = tk.Frame(root)
    button_frame.pack()
    create_buttons(button_frame, panel)
    root.mainloop()

main()
