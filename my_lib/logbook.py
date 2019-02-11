################################################################################
#   logbook.py
#
#   Class Logbook for output messages
#
#   11.02.2019  Created by: zhenya
################################################################################
import time

class Logbook():
    def __init__(self):
        pass

    # Timestamp message
    def log(message):
        print(time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())), message)
