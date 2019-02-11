################################################################################
#   applicaition.py
#
#   This module initializes the App
#
#   11.02.2019  Created by:  zhenya
################################################################################
from game     import *
from game_gui import *

class Application:
  def __init__(self):
    self.root = Tk()
    self.game = Game()
    self.gui  = GameGUI(self.root, self.game)