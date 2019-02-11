################################################################################
#   bounce.py
#
#   App main module
#
#   11.02.2019  Created by: zhenya
################################################################################
from application    import *
from my_lib.logbook import *

if __name__ == "__main__":
    Logbook.log("Game is starting")
  
    app = Application()
  
    app.root.mainloop()
  
    Logbook.log("Game is over")