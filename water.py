#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback_rising(channel):
 
#    import pdb;pdb.set_trace()
    print '-----------------------------'
    print 'rising --- %s channel --- ' % channel,
    response = GPIO.input(channel)
    if response:
        print "No water detected!"
    else:
        print "Water detected!"
    print '-----------------------------'

def callback_falling(channel):
 
    print '-----------------------------'
    print 'falling --- %s channel --- ' % channel,
    if GPIO.input(channel):
        print "input detected!"
    else:
        print "no input detected!"
    print '-----------------------------'

#GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback_rising)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)