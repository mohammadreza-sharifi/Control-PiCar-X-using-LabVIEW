import sys
from robot_hat import TTS 
from picarx import Picarx
import random
from time import sleep

responseList = ["hello world","hi there","nice to meet you","hi again","my name is pi car x","i am a smart robot"]
#print(sys.argv[1])
ttsbot = TTS()
px = Picarx()

if sys.argv[1] == "say":
    msg = random.choices(responseList)
    ttsbot.say(msg)
    

if sys.argv[1] == "f":
    #ttsbot.say("i recieved number one")
    px.forward(0)
    px.forward(1)
    #sleep(0.5)
    #px.forward(0)
    
    
if sys.argv[1] == "b":
    px.forward(0)
    px.forward(-1)
    
if sys.argv[1] == "sr":
    px.set_camera_servo1_angle(0)
    px.set_camera_servo1_angle(45)
    
if sys.argv[1] == "sl":
    px.set_camera_servo1_angle(0)
    px.set_camera_servo1_angle(-45)
    
if sys.argv[1] == "gr":
    px.forward(0)
    px.set_dir_servo_angle(0)
    px.set_dir_servo_angle(45)
    px.forward(1)

if sys.argv[1] == "gl":
    px.forward(0)
    px.set_dir_servo_angle(0)
    px.set_dir_servo_angle(-45)
    px.forward(1)
    
if sys.argv[1] == "su":
    px.set_camera_servo2_angle(0)
    px.set_camera_servo2_angle(45)
    
if sys.argv[1] == "sd":
    px.set_camera_servo2_angle(0)
    px.set_camera_servo2_angle(-45)
    
if sys.argv[1] == "s":
    px.forward(0)
    px.set_camera_servo1_angle(0)
    px.set_dir_servo_angle(0)
    px.set_camera_servo2_angle(0)
    
