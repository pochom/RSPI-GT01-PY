# -*- coding: utf-8 -*-

import serial
import time
#import pathlib
import RPi.GPIO as GPIO
import datetime

#GPIO Init
RELAY = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY,GPIO.OUT)
GPIO.output(RELAY, GPIO.LOW)

#Serial Port Init
ser = serial.Serial('/dev/ttyUSB0', 115200)
ser_timeout = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)


#Smart Monitor Check
def SM_Check():
    #Variables
    TEST_RESULT = "PASS"
    TIME_START = time.time()
    TIME_CURRENT = time.time()

    #"s820_mk"のログを待機しつつシリアルログ出力"
    print("Test started.")
    print("28VDC is ON.")

    #RELAY ON (28V ON)
    GPIO.output(RELAY, GPIO.HIGH)


    while TIME_CURRENT - TIME_START < 120:
        #print("Time delta:" + str(TIME_CURRENT - TIME_START))
        try:
            data = ser_timeout.readline().strip().decode('utf-8')
            #print(data)
        #電源投入時のノイズに対する例外処理
        except UnicodeDecodeError:
            ser.reset_input_buffer()
            data = ""
        #print(data)
        TIME_CURRENT = time.time()
        if "s820_mk login:" in data:
            #print("Test result is Pass. s820 login log is detected.")
            TEST_RESULT = "PASS"
            break
   
    else:
        #print("Test result is fail")
        TEST_RESULT = "FAIL"
    
    time.sleep(2)
    #RELAY OFF (28V OFF)
    print("28VDC is OFF.")
    GPIO.output(RELAY, GPIO.LOW)
    time.sleep(5)

    return TEST_RESULT


#Main Loop

def Main():
    #Counter Init
    CNT_TOTAL = 0
    CNT_PASS = 0
    CNT_FAIL = 0
    
    try:
        while True:
            TR = SM_Check()
            #print(TR)
            if TR == "PASS":
                CNT_TOTAL += 1
                CNT_PASS += 1
            elif TR == "FAIL":
                CNT_TOTAL += 1
                CNT_FAIL += 1
            print("")
            print("################")
            print("Total Test: " + str(CNT_TOTAL))
            print("Pass: " + str(CNT_PASS))
            print("Fail: " + str(CNT_FAIL))
            print("################")
            print("")
    except KeyboardInterrupt:
        print("Test has been interrupted.")
        GPIO.cleanup()


if __name__ == "__main__":
    Main()
