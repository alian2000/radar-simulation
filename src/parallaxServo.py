
#Example Servo Code
#Control the angle of a
#Servo Motor with Raspberry Pi

# free for use without warranty
# www.learnrobotics.org

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(12, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 0.00001
    tpulse =10* angle+620
    #duty= angle/tpulse
    GPIO.output(12, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(12, False)
    pwm.ChangeDutyCycle(duty)

count = 0
numLoops = 100

while count < numLoops:
    #print("set to 90-deg")
    #setAngle(90)
    #pwm.ChangeDutyCycle(7.541)
    #sleep(1)


    print("set to 0-deg")
    setAngle(0)
    #pwm.ChangeDutyCycle(3.5)
    #sleep(1)
    #print("set to 90-deg")
    #setAngle(0)
    #pwm.ChangeDutyCycle(9)
    #sleep(1)

    print("set to 180-deg")
    setAngle(180)
    #pwm.ChangeDutyCycle(24.1)
    #sleep(1)

    count=count+1

pwm.stop()
GPIO.cleanup()
