################################################################################
#   bat.py
#
#   Model: Bat
#
#   11.02.2019  Created by: zhenya
################################################################################
class Bat():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id     = self.canvas.create_rectangle(0, 0, 100, 10, fill=color, outline=color)
        
        self.canvas.move(self.id, 200, 300)
        self.x = 0        
        self.canvas_width  = self.canvas.winfo_width()

        # Events: press left / right arrows
        self.canvas.bind_all('<KeyPress-Left>',  self.moving_left)
        self.canvas.bind_all('<KeyPress-Right>', self.moving_right)
        
    def move(self):
        self.canvas.move(self.id, self.x, 0)

        pos = self.canvas.coords(self.id)
        if (pos[0] <= 0 or pos[2] >= self.canvas_width): # stop when hits border
          self.x = 0

    def moving_left(self, event):
        self.x = -2

    def moving_right(self, event):
        self.x = 2
