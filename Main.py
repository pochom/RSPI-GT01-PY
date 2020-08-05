# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import GPIO_Control as GCM
import RTC
import threading

"""GPIO Control Test
#GPIO SETUP
GCM.gpio_setup()

while True:
    try:
    #Put Main Loop Below
        for i in range(3):
            GCM.led_blink(15, 0.25)
            print(GCM.reset_read())
        for i in range(3):
            GCM.led_blink(10, 0.25)
            print(GCM.reset_read())
        for i in range(3):
            GCM.led_blink(5, 0.25)
            print(GCM.reset_read())
        for i in range(3):
            GCM.led_blink(9, 0.25)
            print(GCM.reset_read())
        for i in range(3):
            GCM.led_blink(6, 0.25)
            print(GCM.reset_read())

        GCM.led_set(1,1)
        time.sleep(0.1)
        GCM.led_set(2,1)
        time.sleep(0.1)
        GCM.led_set(4,1)
        time.sleep(0.1)
        GCM.led_set(8,1)
        time.sleep(0.1)
        GCM.led_set(8,0)
        time.sleep(0.1)
        GCM.led_set(4,0)
        time.sleep(0.1)
        GCM.led_set(2,0)
        time.sleep(0.1)
        GCM.led_set(1,0)
        time.sleep(0.1)
    except KeyboardInterrupt:
        GCM.gpio_cleanup()
"""

#RTC Control
RTC.rtc_init()
RTC.rtc_set()
time.sleep(1)
print(RTC.rtc_get())

