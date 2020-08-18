# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import GPIO_Control as GCM
import RTC
import Serial_Control as SC
from concurrent.futures import ThreadPoolExecutor

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
    time.sleep(10)

    #マルチスレッド処理(LED blink, GT Test)
    with ThreadPoolExecutor(max_workers=5) as executor:
        thread_tstest = executor.submit(SC.serial_test)
        while thread_tstest.running() == True:
            GCM.blink_led(2, 0.25)
        else :
            tpl = thread_tstest.result()
            result_a = tpl[0]
            result_b = tpl[1]
            result_x = tpl[2]
            criteria = tpl[3]
            GCM.led_set(15, 0)


    print("Data numbers in the list: ", end="")
    print(result_a)
    print("Unique position number: ", end="")
    print(result_b)
    print("Unique position rate: ", end="")
    print(str(result_x) + "%")

    if float(result_x) < criteria *100:
        print("Test Result: PASS")
        GCM.led_set(4,1)
    else:
        print("Test Result: FAIL")
        GCM.led_set(8,1)

    
    print("GT Test was correctly finished!!!")
    print("If you would like to run the test again, press reset button.")


def main_function_restart():
    #LED1(init): ON
    GCM.led_set(15,0)
    GCM.led_set(1,1)

    #Serial Login
    #SC.serial_login()
    #time.sleep(10)

    #マルチスレッド処理(LED blink, GT Test)
    with ThreadPoolExecutor(max_workers=5) as executor:
        thread_tstest = executor.submit(SC.serial_test)
        while thread_tstest.running() == True:
            GCM.blink_led(2, 0.25)
        else :
            tpl = thread_tstest.result()
            result_a = tpl[0]
            result_b = tpl[1]
            result_x = tpl[2]
            criteria = tpl[3]
            GCM.led_set(15, 0)


    print("Data numbers in the list: ", end="")
    print(result_a)
    print("Unique position number: ", end="")
    print(result_b)
    print("Unique position rate: ", end="")
    print(str(result_x) + "%")

    if float(result_x) < criteria *100:
        print("Test Result: PASS")
        GCM.led_set(4,1)
    else:
        print("Test Result: FAIL")
        GCM.led_set(8,1)

    
    print("GT Test was correctly finished!!!")
    print("If you would like to run the test again, press reset button.")



if __name__ == '__main__':
    main_init()
    main_function()
    while GCM.reset_read() == 1:
        pass
        time.sleep(0.05)
    else:
        print("Reset button is pressed.")
        main_function_restart()