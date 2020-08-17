# -*- coding: utf-8 -*-

import sys
import RPi.GPIO as GPIO

args = sys.argv

LED1 = 7
LED2 = 1
LED3 = 12
LED4 = 20
NGEN = 24
RST = 21

def gpio_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(NGEN,GPIO.OUT)

#NGEN Control
def ng_control(logic):
    if logic == "1":
        gpio_setup()
        GPIO.output(NGEN, GPIO.HIGH)
        print("NG is ON")
    elif logic == "0":
        gpio_setup()
        GPIO.output(NGEN, GPIO.LOW)
        print("NG is OFF")

#コマンドライン引数0=OFF, 1=ON
ng_control(args[1])