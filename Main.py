# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import GPIO_Control as GCM
import RTC
import Serial_Control as SC
import threading

#GPIO Control Test
#GPIO SETUP
GCM.gpio_setup()

for i in range(1):
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
GCM.gpio_cleanup()


#RTC Control
RTC.rtc_init()
time.sleep(1)
print(RTC.rtc_get())

#Serial Access
SC.serial_login()
result_a, result_b, result_x = SC.serial_test()
print("Data numbers in the list: ", end="")
print(result_a)

print("Unique position number: ", end="")
print(result_b)

print("Unique position rate: ", end="")
print(str(result_x) + "%")

print("Position data was correctly captured!!!")

GCM.gpio_cleanup()