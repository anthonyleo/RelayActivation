#<<<<<<< HEAD
# Test script for 3-ch RPi Relay Board
#=======
# Script for 3-ch RPi Relay Board
#>>>>>>> 5bd8b5ff5860aab12ce2ee97396b27227e80d271
from platform import release
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime
from datetime import datetime
import csv
import os
import keyboard
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
#drive = GoogleDrive(gauth)
engageSleep = 0
releaseSleep = 0

#<<<<<<< HEAD
def cycleRelays():
    # Relays are active-low
    GPIO.output(relay1,True)
    sleep(engageSleep)            

    GPIO.output(relay1,False)
    sleep(releaseSleep)
    #if rigType == "2":
    #    camera.start_preview()
    #    sleep(5)
    #    camera.capture('photo.jpg')

    #    photo = drive.CreateFile({pressCounter: 'photo.jpg'})
    #    photo.SetContentFile('photo.jpg')
    #    photo.Upload()
    
    return

def getTimeStamp():
    today = datetime.now()
    s1 = today.strftime("%d/%m/%y , %H:%M:%S")

    return s1



pressCounter = 1
#>>>>>>> 5bd8b5ff5860aab12ce2ee97396b27227e80d271

# Relay channel definitions
relay1 = 26
#relay2 = 20 but not in use
#relay3 = 21 but not in use

# Initialise GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relay1,GPIO.OUT)
#GPIO.setup(relay2,GPIO.OUT) but relay 2 not in use
#GPIO.setup(relay3,GPIO.OUT) but relay 3 not in use

#<<<<<<< HEAD
print("Specify test rig, type:")
print("'1' for Button Press, or")
print("'2' for Lifter, or")
print("'3' for Lid Rotation")
rigType = input("")
f= open("cycleInfo.txt","w+")
if rigType == "1":    #Button delays
    engageSleep = 1
    releaseSleep = 1
elif rigType == "2":  #Lifter delays
    engageSleep = 3
    releaseSleep = 3
    #camera = PiCamera()
    #camera.resolution = (640, 480)
else:               #Lid Rotation delays
    engageSleep = 3
    releaseSleep = 6

numCycles = input("Enter number of desired cycles. ")
print("Test starting.")

if len(numCycles) == 0:
    infCycleFlag = 1
else:
    numberCycles = int(numCycles)
    infCycleFlag = 0

try:
    if infCycleFlag == 1:
        while 1:
            
            
            cycleRelays()
            f.write("\nCycled relays #" + str(pressCounter) + " | Time Stamp: " + str(getTimeStamp()))
            print("Cycled relays #", pressCounter, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1

        
    elif infCycleFlag == 0:
        while pressCounter <= numberCycles:

            cycleRelays()
            f.write("\nCycled relays #" + str(pressCounter) + " | Time Stamp: " + str(getTimeStamp()))
            print("Cycled relays #", pressCounter, "of", numberCycles, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1
    
        print(numberCycles, " Cycles completed")
        #camera.stop_recording()
#=======

#try:
#    while True:
        
#        cycleRelays()
        # Relays are active-low
        #GPIO.output(relay1,True)
        #sleep(3)

#        print("Cycling relays #", pressCounter)
        #GPIO.output(relay1,False)
        #sleep(5)
#        pressCounter = pressCounter + 1
#>>>>>>> 5bd8b5ff5860aab12ce2ee97396b27227e80d271
    
except KeyboardInterrupt:
    print("Buttons were pressed", pressCounter, "times")
    GPIO.cleanup()
