#Process Implementation

# lab 5
# TimeServer:  
# Name: Jatin K rai
#DawID

"""
Process Implementation: This class implements the Process interface. It maintains:
• A local clock.
• A reference to the TimeServer object.
• It implements methods from the interface:
o synchronize(): Uses RMI to call getTime() on the TimeServer.
 Adjusts the local clock based on the received time and a calculated offset (explained 
later).

Kalman Filter Initialization: The initialize_kalman_filter method sets up the Kalman Filter with initial state, 
state transition matrix, measurement function, covariance matrix, measurement noise, and process noise.
Averaging Samples: The synchronize method now collects multiple time samples from the server and calculates the average server time.
Kalman Filter Update: The offset is calculated and passed through the Kalman Filter to account for network delays and clock drift,
providing a more accurate correction factor.
Clock Adjustment: The local clock is adjusted using the corrected offset from the Kalman Filter.

"""


import Pyro5.api
import time
import numpy as np
from filterpy.kalman import KalmanFilter
from Lib.iLab5Process import iLab5Process

@Pyro5.api.expose
class clsLab5Process (iLab5Process):

    MyProcessName = "P"

    #constructor
    def __init__(self, time_server, currentProcessName):
        self.local_clock = time.time()
        self.time_server = time_server
        self.MyProcessName = currentProcessName
        self.kf = self.initialize_kalman_filter()
        self.time_server.register(currentProcessName)

    """
        The process retrieves the current time from the server using RMI.
        o It calculates the time difference (offset) between the received time and its local clock.
        o It adjusts the local clock by applying a correction factor based on the offset.
         This correction factor might involve averaging multiple samples or using more 
        sophisticated algorithms 
        (e.g., Kalman Filter) to account for network delays and clock 
        drift.
            
    """
    # Kalman Filter) to account for network delays and clock 
    def initialize_kalman_filter(self):
        try:
            print(f"clsLab5Process initialize_kalman_filter function started ")
            kf = KalmanFilter(dim_x=2, dim_z=1)
            kf.x = np.array([[0.], [0.]])  # initial state (location and velocity)
            kf.F = np.array([[1., 1.], [0., 1.]])  # state transition matrix
            kf.H = np.array([[1., 0.]])  # measurement function
            kf.P *= 1000.  # covariance matrix
            kf.R = 5  # measurement noise
            kf.Q = np.array([[0.1, 0.1], [0.1, 0.1]])  # process noise
            print(f"clsLab5Process initialize_kalman_filter function finished ")
            return kf
        except Exception as error:
            print(f" Error from clsLab5Process  initialize_kalman_filter function : {error}")

    def synchronize(self):
        print(f"clsLab5Process synchronize function started for Process : {self.MyProcessName}")
        try:
            #getting samples for server time.
            samples = [self.time_server.getTime() for _ in range(5)]
            #calcuate average server time
            average_server_time = sum(samples) / len(samples)
            #calcuate offset
            offset = average_server_time - self.local_clock

            # Kalman Filter update
            self.kf.predict()
            self.kf.update(offset)
            corrected_offset = self.kf.x[0][0]

            self.local_clock += corrected_offset
            print(f"Synchronized local clock: {self.local_clock}")
            print(f"Process {self.MyProcessName}: Local clock adjusted by {corrected_offset} seconds.")
        except Exception as error:
             print(f" Error from clsLab5Process  synchronize function : {error}")
        print(f"clsLab5Process synchronize function finished for Process : {self.MyProcessName} ")

