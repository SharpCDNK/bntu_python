import math
import tkinter as tk
from tkinter import messagebox

class GeometricObject:
    def __init__ (self, color = "white", filled = False):
        self._color = color
        self._filled = filled

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self,filled):
        self._filled = filled

    def __str__(self):
        return f"GeometricObject(color = {self._color}, filled = {self._filled})"


class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0, color = "white", filled = False):
        super().__init__(color,filled)

        self._side1 = float(side1)
        self._side2 = float(side2)
        self._side3 = float(side3)

    def getSide1(self):
        return self._side1

    def setSide1(self,val):
        self._side1 = val

    def getSide2(self):
        return self._side2

    def setSide2(self,val):
        self._side2 = val

    def getSide3(self):
        return self._side3

    def setSide3(self,val):
        self._side3 = val

    def getArea(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        area = math.sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))
        return area

    def getPerimeter(self):
        return self._side1 + self._side2 + self._side3

    def __str__(self):
        return f"Triangle: side1 = {self._side1} side2 = {self._side2} side3 = {self._side3}"

def calculate_triangle():
    try:
        side1 = float(entry_side1.get())
        side2 = float(entry_side2.get())
        side3 = float(entry_side3.get())

        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            messagebox.showerror("Ошибка", "Введённые стороны не формируют корректный треугольник!")
            return

        color = entry_color.get()
        filled = bool(filled_var.get())

        triangle = Triangle()
        triangle.setSide1(side1)
        triangle.setSide2(side2)
        triangle.setSide3(side3)
        triangle.setColor(color)
        triangle.setFilled(filled)

        area = triangle.getArea()
        perimeter = triangle.getPerimeter()

        result_text = (
            f"Свойства треугольника:\n"
            f"{triangle}\n"
            f"Площадь: {area:.2f}\n"
            f"Периметр: {perimeter:.2f}\n"
            f"Цвет: {triangle.getColor()}\n"
            f"Заполнен: {triangle.isFilled()}"
        )
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения для сторон.")
        return

root = tk.Tk()
root.title("Калькулятор треугольника")

label_title = tk.Label(root, text="Введите данные треугольника", font=("Arial", 14))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_side1 = tk.Label(root, text="Сторона 1:")
label_side1.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_side1 = tk.Entry(root)
entry_side1.grid(row=1, column=1, padx=5, pady=5)

label_side2 = tk.Label(root, text="Сторона 2:")
label_side2.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_side2 = tk.Entry(root)
entry_side2.grid(row=2, column=1, padx=5, pady=5)

label_side3 = tk.Label(root, text="Сторона 3:")
label_side3.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_side3 = tk.Entry(root)
entry_side3.grid(row=3, column=1, padx=5, pady=5)

label_color = tk.Label(root, text="Цвет:")
label_color.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_color = tk.Entry(root)
entry_color.grid(row=4, column=1, padx=5, pady=5)

filled_var = tk.IntVar()
check_filled = tk.Checkbutton(root, text="Заполнен", variable=filled_var)
check_filled.grid(row=5, column=1, sticky="w", padx=5, pady=5)

button_calculate = tk.Button(root, text="Создать треугольник", command=calculate_triangle)
button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
