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

engageSleep = 0
releaseSleep = 0
cycleCount = 0

#<<<<<<< HEAD
def cycleRelays(c):
    # Relays are active-low
    GPIO.output(relayArray[c-1],True)
    sleep(engageSleep)            

    GPIO.output(relayArray[c-1],False)
    sleep(releaseSleep)

    #    camera.start_preview()
    #    sleep(5)
    #    camera.capture('photo.jpg')
    
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
GPIO.setup(14,GPIO.IN)              #TX pin max status
GPIO.setup(15,GPIO.IN)              #RX pin max status
GPIO.setup(relayArray[0],GPIO.OUT)  #relay 1
GPIO.setup(relayArray[1],GPIO.OUT)  #relay 2
GPIO.setup(relayArray[2],GPIO.OUT)  #relay 3

#<<<<<<< HEAD
print("Specify test rig, type:")
print("'1' for Button Press, or")
print("'2' for Lifter, or")
print("'3' for Lid Rotation")
rigType = int(input(""))

serial = input("Enter device serial #: ")

if rigType == 1:    #Button delays
    rigName = "ButtonPress"
    engageSleep = 1
    releaseSleep = 1
    testCycles = 102240

elif rigType == 2:  #Lifter delays
    rigName = "LidLifter"
    engageSleep = 3
    releaseSleep = 3
    testCycles = 5112

    #camera = PiCamera()
    #camera.resolution = (640, 480)

else:               #Lid Rotation delays
    rigName = "LidRotate"
    engageSleep = 7
    releaseSleep = 2
    testCycles = 20448

filename = str(datetime.now().strftime("%d-%m-%y")+"_"+rigName+"_cycleInfo_"+serial)
f= open("%s.csv" % filename,"w+")
shutil.move("/home/vbreathe/RelayActivation/"+filename+".csv","/home/vbreathe/RelayActivation/Archive/"+filename+".csv")
f.write("Test "+rigName+" starting...")

print("Please see actuator extension and retraction timer defaults for this test rig:")
print("Extension: "+str(engageSleep)+"s")
print("Retraction: "+str(releaseSleep)+"s")
print("")
if((input("Do you wish to change the extension and retraction time for the actuator from its defaults? (Y/N): ")) == "Y"):
    engageSleep = int(input("Enter new extension time in seconds: "))
    releaseSleep = int(input("Enter new retraction time in seconds: "))

if((input("Test rig using V&V "+str(testCycles)+" test cycles? (Y/N): ")) == "Y"):
    numCycles = testCycles
else:
    numCycles = int(input("Enter number of desired cycles: "))


channel = int(input("Enter relay channel for test (1-3): "))
print("Test starting.")

if numCycles == 0:
    infCycleFlag = 1
else:
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
        while pressCounter <= numCycles:

            cycleRelays(channel)
            f.write("\nCycled relays #" + str(pressCounter) + " | Time Stamp: " + str(getTimeStamp()))
            print("Cycled relays #", pressCounter, "of", numCycles, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1
    
        print(numCycles, " Cycles completed")
        f.close()
        #camera.stop_recording()
#=======

#>>>>>>> 5bd8b5ff5860aab12ce2ee97396b27227e80d271
    
except KeyboardInterrupt:
    print("Buttons were pressed", pressCounter, "times")
    GPIO.cleanup()
