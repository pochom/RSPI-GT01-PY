# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import GPIO_Control as GCM
import threading

#GPIO SETUP
GCM.gpio_setup()


while True:
    try:
    #Put Main Loop Below
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

