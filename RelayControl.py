#<<<<<<< HEAD
# Test script for 3-ch RPi Relay Board
#=======
# Script for 3-ch RPi Relay Board
#>>>>>>> 5bd8b5ff5860aab12ce2ee97396b27227e80d271
import RPi.GPIO as GPIO
from time import sleep
import datetime
from datetime import datetime
import csv
import os
import keyboard

#<<<<<<< HEAD
def cycleRelays():
    # Relays are active-low
    GPIO.output(relay1,True)
    if rigType == 1:    #If rig presser was selected
        sleep(3)
    else:               #Otherwise lifter    
        sleep(6)

    
    GPIO.output(relay1,False)
    if rigType == 1:
        sleep(5)        #If rig presser was selected
    else:
        sleep(10)       #Otherwise lifter  
    
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
rigType = input("Specify test rig, '1' for Button Press or '2' for Lifter? ")
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
            print("Cycled relays #", pressCounter, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1

        
    elif infCycleFlag == 0:
        while pressCounter <= numberCycles:

            cycleRelays()
            print("Cycled relays #", pressCounter, "of", numberCycles, "| Time Stamp:", getTimeStamp())
            pressCounter = pressCounter + 1
    
        print(numberCycles, " Cycles completed")
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
