from adafruit_crickit import crickit			#Crickit hat library 
from adafruit_motor import stepper 				#Crickit hat motor library for stepper motor control
import time

STEP_MOTOR = crickit.stepper_motor #create a stepper motor object for control
INTERSTEP_DELAY = 0.01
STEPS_PER_REV = 200
#note - our motor is Stepper motor - NEMA-17 size - 200 steps/rev, 12V 350mA
#https://www.adafruit.com/product/324

for i in range(200):			#full rotation of stepper, forward
    STEP_MOTOR.onestep(direction=stepper.FORWARD)
    time.sleep(INTERSTEP_DELAY)
    
for i in range(200):			#full rotation of stepper, backward
    STEP_MOTOR.onestep(direction=stepper.BACKWARD)
    time.sleep(INTERSTEP_DELAY)
    
start = time.time()
end = time.time()

while (end - start) < 5:		#using time library to go 'back and forth' for 5s
    for i in range(50):
        STEP_MOTOR.onestep(direction=stepper.FORWARD)
        time.sleep(INTERSTEP_DELAY)
    for i in range(50):
        STEP_MOTOR.onestep(direction=stepper.BACKWARD)
        time.sleep(INTERSTEP_DELAY)
    end = time.time()
    print(end - start)