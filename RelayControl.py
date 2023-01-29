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
import shutil
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
#drive = GoogleDrive(gauth)
engageSleep = 0
releaseSleep = 0

#<<<<<<< HEAD
def cycleRelays(c):
    # Relays are active-low
    GPIO.output(relayArray[c-1],True)
    sleep(engageSleep)            

    GPIO.output(relayArray[c-1],False)
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
relayArray = [26,20,21]

# Initialise GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relayArray[0],GPIO.OUT) #relay 1
GPIO.setup(relayArray[1],GPIO.OUT) #relay 2
GPIO.setup(relayArray[2],GPIO.OUT) #relay 3

#<<<<<<< HEAD
print("Specify test rig, type:")
print("'1' for Button Press, or")
print("'2' for Lifter, or")
print("'3' for Lid Rotation")
rigType = input("")

serial = input("Enter device serial #: ")
filename = "cycleInfo_"+serial+"_"+str(rigType)+"_"+str(datetime.now().strftime("%d-%m-%y"))
f= open("%s.csv" % filename,"w+")
shutil.move("/home/vbreathe/RelayActivation/"+filename+".csv","/home/vbreathe/RelayActivation/Archive/"+filename+".csv")

if rigType == "1":    #Button delays
    engageSleep = 1
    releaseSleep = 1
    testCycles = 102240
    f.write("Button Press Test Rig")
elif rigType == "2":  #Lifter delays
    engageSleep = 3
    releaseSleep = 3
    testCycles = 5112
    f.write("Lifting Test Rig")
    #camera = PiCamera()
    #camera.resolution = (640, 480)
else:               #Lid Rotation delays
    engageSleep = 6
    releaseSleep = 2
    testCycles = 20448
    f.write("Lid Rotation Test Rig")

print("Please see actuator extension and retraction timer defaults for this test rig:")
print("Extension: "+str(engageSleep)+" s")
print("Retraction: "+str(releaseSleep)+" s")
print("")
if((input("Do you wish to change the extension and retraction time for the actuator from its defaults? (Y/N): ")) == "Y"):
    engageSleep = int(input("Enter new extension time in seconds: "))
    releaseSleep = int(input("Enter new retraction time in seconds: "))

if((input("Test rig using V&V "+str(testCycles)+" test cycles? (Y/N): ")) == "Y"):
    numCycles = testCycles
else:
    numCycles = input("Enter number of desired cycles: ")


channel = int(input("Enter relay channel for test (1-3):"))
print("Test starting.")

if len(numCycles) == 0:
    infCycleFlag = 1
else:
    numberCycles = int(numCycles)
    infCycleFlag = 0

try:
    if infCycleFlag == 1:
        while 1:
            
            
            cycleRelays(channel)
            f.write("\nCycled relays #" + str(pressCounter) + " | Time Stamp: " + str(getTimeStamp()))
            print("Cycled relays #", pressCounter, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1

        f.close()
        
    elif infCycleFlag == 0:
        while pressCounter <= numberCycles:

            cycleRelays(channel)
            f.write("\nCycled relays #" + str(pressCounter) + " | Time Stamp: " + str(getTimeStamp()))
            print("Cycled relays #", pressCounter, "of", numberCycles, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1
    
        print(numberCycles, " Cycles completed")
        f.close()
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
