import tkinter as tk

import numpy
import sklearn

from digits import train

class DrawableGrid(tk.Frame):
    def __init__(self, parent, width, height, size=5):
        super().__init__(parent, bd=1, relief="sunken")
        self.width = width
        self.height = height
        self.size = size
        canvas_width = width*size
        canvas_height = height*size
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, width=canvas_width, height=canvas_height)
        self.canvas.pack(fill="both", expand=True, padx=2, pady=2)

        for row in range(self.height):
            for column in range(self.width):
                x0, y0 = (column * size), (row*size)
                x1, y1 = (x0 + size), (y0 + size)
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill="white", outline="gray",
                                             tags=(self._tag(row, column),"cell" ))
        self.canvas.tag_bind("cell", "<B1-Motion>", self.paint)
        self.canvas.tag_bind("cell", "<1>", self.paint)

    def _tag(self, row, column):
        """Return the tag for a given row and column"""
        tag = f"{row},{column}"
        return tag

    def get_pixels(self):
        map = []
        for row in range(self.height):
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                value = 1 if color == "black" else 0
                map.append(value)
        
        print(f"Input: {map}")
        res = container.consume(map)

        output = []
        for i in range(len(res)):
            output.append({'num': i, 'out': round(res[i], 2)})
        output.sort(key = lambda k : k['out'], reverse=True)

        print(f"Output: {output}")

        print('------------------------------------')

    def paint(self, event):
        cell = self.canvas.find_closest(event.x, event.y)
        color = self.canvas.itemcget(cell, "fill")
        new_color = "black" if color=="white" else "white"
        self.canvas.itemconfigure(cell, fill=new_color)

    def paint_xy(self, x, y):
        cell = self.canvas.find_closest(x*PIXEL_SIZE, y*PIXEL_SIZE)
        self.canvas.itemconfigure(cell, fill="black")

# Prepare GUI

WIDTH = 5
HEIGHT = 7
PIXEL_SIZE = 70

root = tk.Tk()

input_frame = tk.Frame(root)
input_frame.pack(side = tk.LEFT)

title = tk.Text(input_frame, height=1, width=20)
title.insert(tk.INSERT, "Input:")
title.pack()

canvas = DrawableGrid(input_frame, width=WIDTH, height=HEIGHT, size=PIXEL_SIZE)

apply_button = tk.Button(input_frame, text="Apply", command=canvas.get_pixels, fg="green")
apply_button.pack(side="bottom")

clear_button = tk.Button(input_frame, text="Clear", command=canvas.get_pixels, fg="red")
clear_button.pack(side="bottom")

output_frame = tk.Frame(root)
output_frame.pack(side = tk.LEFT)

title2 = tk.Text(output_frame, height=1, width=20)
title2.insert(tk.INSERT, "Prediction:")
title2.pack(side="top")

canvas.pack(fill="both", expand=True)

# Read training data from file

psi = [[],[],[],[],[],[],[],[],[],[]]   # 10 x 35
zeta = numpy.identity(10).tolist()

with open("../inputs/digits_map_train_set.txt", "r") as f:
    line_num = 0 
    for line in f.readlines():
        psi_num = line_num // 7
        for pixel in line.split(" "):
            psi[psi_num].append(int(pixel))
        line_num +=1

i = 0
for pixel in psi[0]:
    if pixel:
        cell = canvas.paint_xy(i%5, i//5)
    i += 1

container = train(psi, zeta, False)

# Run GUI

root.mainloop()