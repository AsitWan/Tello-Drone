# Basic Tello Navigation

from djitellopy import tello
nav=tello.Tello()
nav.connect()
print("Battery%:", nav.get_battery())
nav.get_battery()

#This is manuel instruction to the Drone:-
import time
nav.takeoff()
time.sleep(2)   # Adds delays as needed
nav.flip_forward()
time.sleep(2)
nav.send_rc_control(0, 30, 0, 0)
time.sleep(2)
nav.flip_right()
time.sleep(2)
nav.send_rc_control(30,0,0,0)
time.sleep(2)
nav.flip_back()
time.sleep(2)
nav.move_back(30)
time.sleep(2)
nav.flip_left()
time.sleep(2)
nav.send_rc_control(-30, 0, 0, 0)
nav.land()
