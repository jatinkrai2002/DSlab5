#Server Setup

# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID


import Pyro5.api
from Lib.clsLab5TimeServer import clsLab5TimeServer
from Lib.URLHelper import URLHelper
from pathlib import Path
import os

def Start_Lab5TimeServer_srv():
    #Act as Server.
    try:
        #make it server ready for remote process.
        daemon = Pyro5.api.Daemon()

    except Exception as error:
        print("Pyro5.api.Daemo(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo(): completed successfully.")

    try:
        #make it server ready for remote process.
        # Register TimeServer
        time_server = clsLab5TimeServer()
        uri = daemon.register(time_server)

        print (f"URI of the TimeServer is : {uri}")

        #write to the URLFile folder

      
        currentworkingdir = os.getcwd()
        """
            data_folder = Path("source_data/text_files/")
            file_to_open = data_folder / "raw_data.txt"
            print(file_to_open.read_text())
        """

        URLPath = currentworkingdir + "\\ServerOutput\\UrlfileforTimeServer.txt"
        URLFileObj = URLHelper(URLPath)
        URLFileObj.writeServerURLFile(str(uri))

    except Exception as error:
        print("Pyro5.api.Daemo.register(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.register() : completed successfully.")

    try:
        #make it server ready for remote process.
        print("UnicastRemoteObject for timeServer Protocol=" , uri)
        print("Time Server registered. Ready.")
        daemon.requestLoop()  # Start the event loop of 
    except Exception as error:
        print("Pyro5.api.Daemo.requestLoop(): failed.")
        print(error)
    finally:
        print("Pyro5.api.Daemo.requestLoop() : completed successfully.")

if __name__ == "__main__":
    Start_Lab5TimeServer_srv()