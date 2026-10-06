'''import tkinter as tk
root = tk.Tk()
root.geometry("600x450")
canvas = tk.Canvas(root, width=550, height=360, bg="white")
canvas.pack()
canvas.create_rectangle(40, 40, 220, 150, fill="coral")
canvas.create_oval(280, 50, 440, 190, fill="lightblue")
canvas.create_line(50, 250, 500, 250, width=4)
canvas.create_text(275, 310, text="Hello Canvas", font=
("Arial", 20))
root.mainloop();'''

import tkinter as tk

# Create window
window = tk.Tk()
window.title("Simple House")
window.geometry("600x500")

# Create canvas
canvas = tk.Canvas(window, width=600, height=500, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 400, 600, 500, fill="green")

# House body
canvas.create_rectangle(180, 220, 420, 400, fill="lightyellow", outline="black")

# Roof
canvas.create_polygon(
    150, 220,
    300, 100,
    450, 220,
    fill="red",
    outline="black"
)

# Door
canvas.create_rectangle(275, 310, 325, 400, fill="brown", outline="black")

# Door knob
canvas.create_oval(312, 350, 318, 356, fill="yellow")

# Left window
canvas.create_rectangle(210, 260, 260, 310, fill="lightblue", outline="black")
canvas.create_line(235, 260, 235, 310, fill="black")
canvas.create_line(210, 285, 260, 285, fill="black")

# Right window
canvas.create_rectangle(340, 260, 390, 310, fill="lightblue", outline="black")
canvas.create_line(365, 260, 365, 310, fill="black")
canvas.create_line(340, 285, 390, 285, fill="black")

# Sun
canvas.create_oval(480, 50, 540, 110, fill="yellow", outline="orange")

# Tree
canvas.create_rectangle(80, 300, 105, 400, fill="brown")
canvas.create_oval(45, 240, 140, 330, fill="darkgreen", outline="black")

# Run the window
window.mainloop()

