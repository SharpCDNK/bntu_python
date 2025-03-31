from tkinter import *
import math
import time

class Stil1Clock(Canvas):
    def __init__(self, master, width=200, height=200, bg="white", **kwargs):
        super().__init__(master, width=width, height=height, bg=bg, **kwargs)
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.radius = min(width, height) // 2 - 10

        current_time = time.localtime()
        self.hour = current_time.tm_hour % 12  # Приводим часы к 12-часовому формату
        self.minute = current_time.tm_min
        self.second = current_time.tm_sec

        self.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                         self.center_x + self.radius, self.center_y + self.radius,
                         outline="black", width=2)

        for i in range(12):
            angle = math.radians(i * 30)
            x = self.center_x + self.radius * 0.8 * math.cos(angle)
            y = self.center_y - self.radius * 0.8 * math.sin(angle)
            self.create_text(x, y, text=str(i + 1), font=("Arial", 12))

        self.hour_hand = self.create_line(self.center_x, self.center_y,
                                          self.center_x, self.center_y - self.radius * 0.5,
                                          fill="black", width=4)
        self.minute_hand = self.create_line(self.center_x, self.center_y,
                                            self.center_x, self.center_y - self.radius * 0.7,
                                            fill="blue", width=2)
        self.second_hand = self.create_line(self.center_x, self.center_y,
                                            self.center_x, self.center_y - self.radius * 0.9,
                                            fill="red", width=1)

        self.update_clock()

    def update_clock(self):
        hour_angle = math.radians((self.hour + self.minute / 60) * 30 - 90)
        hour_x = self.center_x + self.radius * 0.5 * math.cos(hour_angle)
        hour_y = self.center_y + self.radius * 0.5 * math.sin(hour_angle)
        self.coords(self.hour_hand, self.center_x, self.center_y, hour_x, hour_y)

        minute_angle = math.radians(self.minute * 6 - 90)
        minute_x = self.center_x + self.radius * 0.7 * math.cos(minute_angle)
        minute_y = self.center_y + self.radius * 0.7 * math.sin(minute_angle)
        self.coords(self.minute_hand, self.center_x, self.center_y, minute_x, minute_y)

        second_angle = math.radians(self.second * 6 - 90)
        second_x = self.center_x + self.radius * 0.9 * math.cos(second_angle)
        second_y = self.center_y + self.radius * 0.9 * math.sin(second_angle)
        self.coords(self.second_hand, self.center_x, self.center_y, second_x, second_y)

    def setHour(self, hour):
        self.hour = hour % 12
        self.update_clock()

    def setMinute(self, minute):
        self.minute = minute % 60
        self.update_clock()

    def setSecond(self, second):
        self.second = second % 60
        self.update_clock()

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second


class DisplayClocks:
    def __init__(self):
        self.window = Tk()
        self.window.title("Group of Clocks")

        clocks_frame = Frame(self.window)
        clocks_frame.pack(padx=10, pady=10)

        self.clocks = []
        for i in range(4):
            clock = Stil1Clock(clocks_frame, width=200, height=200, bg="white")
            clock.grid(row=0, column=i, padx=10, pady=10)
            self.clocks.append(clock)

        control_frame = Frame(self.window)
        control_frame.pack(pady=10)

        Label(control_frame, text="Hour:").grid(row=0, column=0)
        self.hour = IntVar()
        self.hour.set(self.clocks[0].getHour())
        Entry(control_frame, textvariable=self.hour, width=3).grid(row=0, column=1)

        Label(control_frame, text="Minute:").grid(row=0, column=2)
        self.minute = IntVar()
        self.minute.set(self.clocks[0].getMinute())
        Entry(control_frame, textvariable=self.minute, width=3).grid(row=0, column=3)

        Label(control_frame, text="Second:").grid(row=0, column=4)
        self.second = IntVar()
        self.second.set(self.clocks[0].getSecond())
        Entry(control_frame, textvariable=self.second, width=3).grid(row=0, column=5)

        Button(control_frame, text="Set New Time", command=self.setNewTime).grid(row=0, column=6, padx=5)

        self.window.mainloop()

    def setNewTime(self):
        new_hour = self.hour.get()
        new_minute = self.minute.get()
        new_second = self.second.get()
        for clock in self.clocks:
            clock.setHour(new_hour)
            clock.setMinute(new_minute)
            clock.setSecond(new_second)

DisplayClocks()
