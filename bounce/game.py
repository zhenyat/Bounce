################################################################################
#   game.py
#
#   Game controller
#
#   11.02.2019  Created by: zhenya
################################################################################
import time
from my_lib.logbook import *
from ball           import *
from bat            import *

class Game():
    def __init__(self):
        pass

    def go(self, gui_object):
        try:
            while(True):
                gui_object.ball.move()
                gui_object.bat.move()
                gui_object.master.update() 
                time.sleep(0.05)
        except:
            Logbook.log("Game has been aborted")            
