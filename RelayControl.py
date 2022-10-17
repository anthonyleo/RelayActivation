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
    if rigType == "P":
        sleep(3)
    else:
        sleep(6)

    
    GPIO.output(relay1,False)
    if rigType == "P":
        sleep(5)
    else:
        sleep(10)
    
    return


pressCounter = 1
#=======

pressCounter = 0
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
rigType = input("Specify test rig, 'P' for Press or 'L' for Lifter? ")
numCycles = input("Enter number of desired cycles. ")

if len(numCycles) == 0:
    infCycleFlag = 1
else:
    numberCycles = int(numCycles)
    infCycleFlag = 0

try:
    if infCycleFlag == 1:
        while 1:
            
            today = datetime.datetime.now()
            s1 = today.strftime("%d/%m/%y , %H:%M:%S")
            cycleRelays()
            print("Cycled relays #", pressCounter, ". Time Stamp: ", s1)
            pressCounter = pressCounter + 1

        
    elif infCycleFlag == 0:
        while pressCounter <= numberCycles:

            today = datetime.datetime.now()
            s1 = today.strftime("%d/%m/%y , %H:%M:%S")
            cycleRelays()
            print("Cycled relays #", pressCounter, "of", numberCycles, ". Time Stamp: ", s1)
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
