#Process Logic

# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID


import Pyro5.api
from Lib.clsLab5Process import clsLab5Process
from Lib.URLHelper import URLHelper
from pathlib import Path
import os


def Start_TimeServerProcessClient():
    try:
        MyProcessName = "P1"
        currentworkingdir = os.getcwd()
        """
            data_folder = Path("source_data/text_files/")
            file_to_open = data_folder / "raw_data.txt"
            print(file_to_open.read_text())
        """
        #read url from file
        URLPath = currentworkingdir + "\\ServerOutput\\UrlfileforTimeServer.txt"
        URLFileObj = URLHelper(URLPath)
        uri = URLFileObj.readserverURLFile()

        if ((uri is None) or (len(uri) < 1)):
            uri = input("Enter the UnicastRemoteObject for Time Server URI: ")

        print (f"URI of the TimeServer is : {uri}")    
        time_server = Pyro5.api.Proxy(uri)
        
        if(time_server is None):
                print(f" URI is not valid : {uri} ")
        else:
            remote_process = clsLab5Process(time_server, MyProcessName)

            print ("clsLab5 Time Server has started for Process")
            
            print ("clsLab5TimeServer:Synchronize process has started")
            # Simulate critical section work
            remote_process.synchronize()
            print ("clsLab5TimeServer:Synchronize process has Completed")

            print ("clsLab5 Time Server has completed for Process")
        
    except Exception as error:
                print("Pyro5.api.Proxy(): lsLab5TimeServer:Synchronize.Proxy failed while calling")
                print (error)
    finally:
                print("Pyro5.api.Proxy(): ClockArry Pyro5.api.Proxy completed successfully while calling.")

if __name__ == "__main__":
    Start_TimeServerProcessClient()
