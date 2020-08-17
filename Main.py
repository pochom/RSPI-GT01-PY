# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import GPIO_Control as GCM
import RTC
import Serial_Control as SC
import threading

def main_init():
    #GPIO SETUP
    GCM.gpio_setup()

    #RTC Control
    #RTC.rtc_init()
    #time.sleep(1)
    #print(RTC.rtc_get())


def main_function():
    #LED1(init): ON
    GCM.led_set(15,0)
    GCM.led_set(1,1)

    #Serial Login
    SC.serial_login()

    #マルチスレッド処理(LED blink, GT Test)
    thread_led2_blink = threading.Thread(target=GCM.led_blink(2,0.5))
    thread_login = threading.Thread(target=result_a, result_b, result_x, criteria = SC.serial_test())
    thread_led2_blink.start()
    thread_login.start()
    thread_login.join()
    thread_led2_blink.stop()

    print("Data numbers in the list: ", end="")
    print(result_a)
    print("Unique position number: ", end="")
    print(result_b)
    print("Unique position rate: ", end="")
    print(str(result_x) + "%")

    if float(result_x) < criteria *100:
        print("Test Result: PASS")
        GCM.led_set(15,0)
        GCM.led_set(4,1)
    else:
        print("Test Result: FAIL")
        GCM.led_set(15,0)
        GCM.led_set(8,1)

    print("GT Test was correctly finished!!!")
    print("If you would like to run the test again, press reset button.")




if __name__ == '__main__':
    while True:
        main_init()
        main_function()
        while GCM.reset_read() == 1:
            pass
            time.sleep(0.05)
        else:
            break