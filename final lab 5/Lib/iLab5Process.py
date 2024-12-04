#Process Interface
# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID


"""
Process Interface: This interface defines methods for processes to synchronize their clocks. Methods can 
include:
• synchronize(): Requests the current time from the time server.

"""

import Pyro5.api

@Pyro5.api.expose
class iLab5Process:
    #synchronize(): Requests the current time from the time server.
    def synchronize(self):
        pass