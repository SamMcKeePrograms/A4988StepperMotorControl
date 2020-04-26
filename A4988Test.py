import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

MS3 = 26
MS2 = 19
MS1 = 13
enable = 6
step = 20 
direct = 21 

GPIO.setup(enable, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.setup(direct, GPIO.OUT)
GPIO.setup(MS3, GPIO.OUT)
GPIO.setup(MS2, GPIO.OUT)
GPIO.setup(MS1, GPIO.OUT)

def fullStep():
    GPIO.output(MS1, GPIO.LOW)
    GPIO.output(MS2, GPIO.LOW)
    GPIO.output(MS3, GPIO.LOW)
def halfStep():
    GPIO.output(MS1, GPIO.HIGH)
    GPIO.output(MS2, GPIO.LOW)
    GPIO.output(MS3, GPIO.LOW)
def quarterStep():
    GPIO.output(MS1, GPIO.LOW)
    GPIO.output(MS2, GPIO.HIGH)
    GPIO.output(MS3, GPIO.LOW)
def eightStep():
    GPIO.output(MS1, GPIO.HIGH)
    GPIO.output(MS2, GPIO.HIGH)
    GPIO.output(MS3, GPIO.LOW)
def sixteenthStep():
    GPIO.output(MS1, GPIO.HIGH)
    GPIO.output(MS2, GPIO.HIGH)
    GPIO.output(MS3, GPIO.HIGH)

#you can change the delay to either increase the speed or decrease the speed
#of the motor
delay = .0009
print("please input cw or ccw...")
while True:
    #turns power to the motor off until you input a command
    GPIO.output(enable, GPIO.HIGH)

    sixteenthStep()
      
    answer = input("")
    #clock wise
    if(answer == "cw"):
        #gives power to the motor
        GPIO.output(enable, GPIO.LOW)
        #changes direction to clock wise
        GPIO.output(direct, GPIO.LOW)
        #one rotation with 1.8 degrees per step
        for i in range(200):
            GPIO.output(step, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(step, GPIO.LOW)
            time.sleep(delay)
    #counter clock wise
    elif(answer == "ccw"):
        #gives power to the motor
        GPIO.output(enable, GPIO.LOW)
        #changes direction to counter clock wise
        GPIO.output(direct, GPIO.HIGH)
        #one rotation with 1.8 degrees per step
        for i in range(200):
            GPIO.output(step, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(step, GPIO.LOW)
            time.sleep(delay)

GPIO.cleanup()

