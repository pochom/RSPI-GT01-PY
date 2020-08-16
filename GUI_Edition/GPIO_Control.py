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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1,GPIO.OUT)
    GPIO.setup(LED2,GPIO.OUT)
    GPIO.setup(LED3,GPIO.OUT)
    GPIO.setup(LED4,GPIO.OUT)
    GPIO.setup(NGEN,GPIO.OUT)
    GPIO.setup(RST,GPIO.IN)


#NGEN Control
def ngen_set(logic):
    try:
        if logic == 1:
            GPIO.output(NGEN, GPIO.HIGH)
        elif logic == 0:
            GPIO.output(NGEN, GPIO.LOW)
    except KeyboardInterrupt:
        gpio_cleanup()


#Get RESET Status
def reset_read():
    return GPIO.input(RST)


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

        elif port_hex == 9:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)

        elif port_hex == 10:
            if logic == 1:
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)

        elif port_hex == 11:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)

        elif port_hex == 12:
            if logic == 1:
                GPIO.output(LED3, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED3, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)

        elif port_hex == 13:
            if logic == 1:
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)
                GPIO.output(LED4, GPIO.LOW)


        elif port_hex == 14:
            if logic == 1:
                GPIO.output(LED2, GPIO.HIGH)
                GPIO.output(LED3, GPIO.HIGH)
                GPIO.output(LED4, GPIO.HIGH)
            elif logic == 0:
                GPIO.output(LED2, GPIO.LOW)
                GPIO.output(LED3, GPIO.LOW)
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


#LED Blink
def led_blink(port_hex_blink,blink_period):
    try:
        led_set(port_hex_blink, GPIO.HIGH)
        time.sleep(blink_period)
        led_set(port_hex_blink, GPIO.LOW)
        time.sleep(blink_period)
    except KeyboardInterrupt:
        GPIO.cleanup()


#GPIO Port Clean-up
def gpio_cleanup():
    GPIO.cleanup()