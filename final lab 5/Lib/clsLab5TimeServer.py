#TimeServer Implementation
# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID

"""

TimeServer Implementation: This class implements the TimeServer interface. 

It maintains:
• The system's reference clock.
• A list of registered processes (optional, for monitoring).
• It implements methods from the interface:

"""
import Pyro5.api
import time
from Lib.iLab5TimeServer import iLab5TimeServer

@Pyro5.api.expose
class clsLab5TimeServer (iLab5TimeServer):

    def __init__(self):
        self.reference_clock = time.time()
        self.registered_processes = []

    #getTime(): Returns the current time from the server's reference clock.
    def getTime(self):
        # return TimeServer local time
        localtimeserver = time.time()
        print (f" Local time of the TimeServer is : {localtimeserver} ")
        return localtimeserver

    #register(process) (optional): Adds the process to the list of registered clients.
    def register(self, process):
        try:
            print (f"Process P: {process} is ready to register into TimeServer")
            self.registered_processes.append(process)
            print(f"Process P: {process} is registered into TimeServer")

        except Exception as error:
            print(f" Error from clsLab5TimeServer register function : {error}")
        