#TimeServer Interface

# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID

"""

TimeServer Interface: This interface defines methods for processes to interact with the time server. Methods 
can include:
• getTime(): Retrieves the current time from the server.
• register(process) (optional): Registers a process with the server (useful for tracking connected clients).

"""


import Pyro5.api

@Pyro5.api.expose
class iLab5TimeServer:

    # Retrieves the current time from the server.
    def getTime(self):
        pass

    #register(process) (optional): Registers a process with the server (useful for tracking connected clients).
    def register(self, process):
        pass