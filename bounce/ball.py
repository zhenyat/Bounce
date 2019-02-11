################################################################################
#   ball.py
#
#   Model: ball
#
#   11.02.2019  Created by: zhenya
################################################################################
class Ball():
    def __init__(self, canvas, color):
        self.canvas  = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, outline=color)  # 10,10 - top-left
                                                                                 # 25,25 - bottom-right
        self.canvas.move(self.id, 245, 100)

    def move(self):
        self.canvas.move(self.id, self.x, self.y)