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

    def hit_bat(self, gui_object):
        pos_ball = gui_object.canvas.coords(gui_object.ball.id)
        pos_bat  = gui_object.canvas.coords(gui_object.bat.id)
        
        if (pos_ball[3] >= gui_object.ball.canvas_height):
            gui_object.ball.hit_bottom = True
            
        if (pos_ball[0] > pos_bat[0] and pos_ball[2] < pos_bat[2]):
            if (pos_ball[3] > pos_bat[1] and pos_ball[3] < pos_bat[3]):
                return True

    def go(self, gui_object):
        try:
            while(True):
                if (self.hit_bat(gui_object)):
                    gui_object.ball.y = -gui_object.ball.y  # Ball is reflected

                if (gui_object.ball.hit_bottom):
                    Logbook.log("You've lost!")
                    break

                gui_object.ball.move()
                gui_object.bat.move()
                gui_object.master.update() 
                time.sleep(0.05)
        except:
            Logbook.log("Game has been aborted")            
