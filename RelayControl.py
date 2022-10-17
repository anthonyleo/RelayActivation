# Test script for 3-ch RPi Relay Board
import RPi.GPIO as GPIO
from time import sleep
import datetime
import csv
import os
import keyboard

def cycleRelays():
    # Relays are active-low
    GPIO.output(relay1,True)
    sleep(3)

    GPIO.output(relay1,False)
    sleep(5)
    
    return


pressCounter = 1

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

numCycles = input("Enter number of desired cycles. ")

if len(numCycles) == 0:
    infCycleFlag = 1
else:
    numberCycles = int(numCycles)
    infCycleFlag = 0

try:
    if infCycleFlag == 1:
        while 1:

            cycleRelays()
            print("Cycled relays #", pressCounter)
            pressCounter = pressCounter + 1

        
    elif infCycleFlag == 0:
        while pressCounter <= numberCycles:

            cycleRelays()
            print("Cycled relays #", pressCounter, "of", numberCycles)
            pressCounter = pressCounter + 1
    
        print(numberCycles, " Cycles completed")
    
except KeyboardInterrupt:
    print("Buttons were pressed", pressCounter, "times")
    GPIO.cleanup()
