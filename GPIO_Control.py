# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

LED1 = 7
LED2 = 1
LED3 = 12
LED4 = 20
NGEN = 24
RST = 21

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1,GPIO.OUT)
    GPIO.setup(LED2,GPIO.OUT)
    GPIO.setup(LED3,GPIO.OUT)
    GPIO.setup(LED4,GPIO.OUT)
    GPIO.setup(NGEN,GPIO.OUT)
    GPIO.setup(RST,GPIO.IN)

#Single GPIO OUT Control
def led_set(port_hex,logic):
    try:
        if port_hex == 1:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
        
        elif port_hex == 2:
            if logic == 1:
                GPIO.output(LED2, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED2, GPIO.LOW)

        elif port_hex == 3:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)

        elif port_hex == 4:
            if logic == 1:
                GPIO.output(LED3, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED3, GPIO.LOW)

        elif port_hex == 5:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)

        elif port_hex == 6:
            if logic == 1:
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)

        elif port_hex == 7:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)

        elif port_hex == 8:
            if logic == 1:
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED4, GPIO.LOW)

        elif port_hex == 15:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)

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