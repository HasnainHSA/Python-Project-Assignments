# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the
# screen. We then create an eraser rectangle which, when dragged around the canvas, 
# sets all of the rectangles it is in contact with to white.

import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10
ERASER_SIZE = 60

class CanvasEraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()

        # Draw grid
        self.cells = {}
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                self.cells[rect] = (x1, y1, x2, y2)

        self.eraser = self.canvas.create_rectangle(10, 10, 10 + ERASER_SIZE, 10 + ERASER_SIZE, fill="gray")

        self.canvas.tag_bind(self.eraser, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.eraser, "<B1-Motion>", self.on_drag)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(self.eraser, dx, dy)
        self.start_x = event.x
        self.start_y = event.y
        self.erase_cells()

    def erase_cells(self):
        ex1, ey1, ex2, ey2 = self.canvas.coords(self.eraser)
        for rect, (x1, y1, x2, y2) in self.cells.items():
            if not self.canvas.itemcget(rect, "fill") == "white":

                if not (ex2 < x1 or ex1 > x2 or ey2 < y1 or ey1 > y2):
                    self.canvas.itemconfig(rect, fill="white")

# Start the app
root = tk.Tk()
app = CanvasEraserApp(root)
root.mainloop()
