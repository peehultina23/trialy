

#single led
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 29

GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, True)
    sleep(1)
    GPIO.output(led, False)
    sleep(1)

#multiple led
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED pin numbers (Physical pins)
led1 = 29
led2 = 31
led3 = 33
led4 = 35
led5 = 37

# Setup pins as output
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)

# Initially turn OFF all LEDs
GPIO.output(led1, False)
GPIO.output(led2, False)
GPIO.output(led3, False)
GPIO.output(led4, False)
GPIO.output(led5, False)

def ledpattern(v1, v2, v3, v4, v5):
    GPIO.output(led1, v1)
    GPIO.output(led2, v2)
    GPIO.output(led3, v3)
    GPIO.output(led4, v4)
    GPIO.output(led5, v5)

try:
    while True:
        for _ in range(5):
            ledpattern(1,0,0,0,0)
            sleep(0.5)
            ledpattern(0,1,0,0,0)
            sleep(0.5)
            ledpattern(0,0,1,0,0)
            sleep(0.5)
            ledpattern(0,0,0,1,0)
            sleep(0.5)
            ledpattern(0,0,0,0,1)
            sleep(0.5)

finally:
    GPIO.output(led1, False)
    GPIO.output(led2, False)
    GPIO.output(led3, False)
    GPIO.output(led4, False)
    GPIO.output(led5, False)
    GPIO.cleanup()