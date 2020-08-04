# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

LED1 = 7
LED2 = 1
LED3 = 12
LED4 = 20
NGEN = 24
RST = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(NGEN,GPIO.OUT)
GPIO.setup(RST,GPIO.IN)

#Single GPIO OUT Control
def gpio_write(x,y):
    try:
        if y == 1:
            GPIO.output(x, GPIO.HIGH)
        else:
            GPIO.output(x, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()


#Get GPIO IN Value
def gpio_read(x):
    return GPIO.input(x)


#Single LED Blink
def gpio_blink(x,y):
    try:
        GPIO.output(x, GPIO.HIGH)
        time.sleep(y)
        GPIO.output(x, GPIO.LOW)
        time.sleep(y)
    except KeyboardInterrupt:
        GPIO.cleanup()
        

#Dual LED Blink
def gpio_blink2(x,y,z):
    try:
        GPIO.output(x, GPIO.HIGH)
        GPIO.output(y, GPIO.HIGH)
        time.sleep(z)
        GPIO.output(x, GPIO.LOW)
        GPIO.output(y, GPIO.LOW)
        time.sleep(z)
    except KeyboardInterrupt:
        GPIO.cleanup()


#GPIO Port Clean-up
def gpio_cleanup():
    GPIO.cleanup()
        
        

        

for num in range(5):
    print(gpio_read(RST))
    gpio_blink2(LED2, LED4, 1)
    gpio_write(LED3, 1)
    time.sleep(1)
    gpio_write(LED3, 0)
    print(gpio_read(RST))
    
gpio_cleanup()