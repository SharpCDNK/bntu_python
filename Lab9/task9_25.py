import tkinter as tk

def change_light():
    canvas.delete("light")
    light = light_var.get()
    colors = {"Red": "gray", "Yellow": "gray", "Green": "gray"}
    if light != "Off":
        colors[light] = light.lower()
    canvas.create_oval(50, 20, 150, 120, fill=colors["Red"], tags="light")
    canvas.create_oval(50, 140, 150, 240, fill=colors["Yellow"], tags="light")
    canvas.create_oval(50, 260, 150, 360, fill=colors["Green"], tags="light")


window = tk.Tk()
window.title("Светофор")

light_var = tk.StringVar(value="Off")


canvas = tk.Canvas(window, width=200, height=400, bg='black')
canvas.pack(side=tk.LEFT, padx=10)


canvas.create_rectangle(40, 10, 160, 370, fill='black')


frame_controls = tk.Frame(window)
frame_controls.pack(pady=20)

tk.Radiobutton(frame_controls, text="Off", variable=light_var, value="Off", command=change_light).pack(anchor=tk.W)
tk.Radiobutton(frame_controls, text="Red", variable=light_var, value="Red", command=change_light).pack(anchor=tk.W)
tk.Radiobutton(frame_controls, text="Yellow", variable=light_var, value="Yellow", command=change_light).pack(anchor=tk.W)
tk.Radiobutton(frame_controls, text="Green", variable=light_var, value="Green", command=change_light).pack(anchor=tk.W)


change_light()

window.mainloop()
