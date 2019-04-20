import RPi.GPIO as GPIO
import time
YELLOW=23
BLUE=14
RED=25
LOOPS=1000
ON_TIME=0.005
OFF_TIME=0.005
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
##print "LED on"
##GPIO.output(18,GPIO.HIGH)
##time.sleep(5)
##print "LED off"
##GPIO.output(18,GPIO.LOW)



def lightLED(output):
    print "LED on", output
    GPIO.output(output,GPIO.HIGH)
    time.sleep(3)
    print "LED off", output
    GPIO.output(output,GPIO.LOW)
    time.sleep(2)


    
def turnon(pin):
    print "LED on", pin
    GPIO.output(pin,GPIO.HIGH)


    
def turnoff(pin):
    print "LED off", pin
    GPIO.output(pin,GPIO.LOW)
    
for i in range(LOOPS):
    if i % 3 == 0:
        print i, " divisible by 3"
        turnon(BLUE)
        time.sleep(ON_TIME)
        turnoff(BLUE)
        time.sleep(OFF_TIME)
        
    if i % 2== 0:
        print i, "divisible by 2"
        turnon(RED)
        time.sleep(ON_TIME)
        turnoff(RED)
        time.sleep(OFF_TIME)


        
    if i % 1== 0:
        print i, "divisible by 1"
        turnon(YELLOW)
        time.sleep(ON_TIME)
        turnoff(YELLOW)
        time.sleep(OFF_TIME)

        
##    turnon(23)
##    turnon(14)
##    turnon(18)
##    time.sleep(0.5)
##    turnoff(23)
##    turnoff(18)
##    turnoff(14)
##    time.sleep(0.25)
turnoff(YELLOW)
turnoff(RED)
turnoff(BLUE)









    
