# A4988StepperMotorControl

#You need to use a bi-polar stepper motor and A4988 stepper motor driver
#If you are planning on using more than 1A then put a heat sink on other wise the chip WILL over heat 
#
#Connections
#GND - ground 
#VDD - Raspberry pi 5V
#1A - one side of the first coil
#1B - the other side of the first coil
#2A - one side of the second coil
#2B - the other side of the first coil
#***This is your power for the stepper motor and it is highly encourage to put a 100 micro faird compacitor to eleavate power spikes***
#GND - ground
#VMOT - 8V to 12V
#DIR - GPIO 21 
#STEP - GPIO 20
#***SLEEP and RESET connect together***
#MS3 - GPIO 26
#MS2 - GPIO 19
#MS1 - GPIO 13

#A4988 has 5 different modes to it fullstep, halfstep, quarterstep, eightstep,and sixteenthstep 

#you can vary the current that goes to the motor by adjusting the limiting screw located near the GND and VDD pins
