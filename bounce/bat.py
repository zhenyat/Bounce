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

