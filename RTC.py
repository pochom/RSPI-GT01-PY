# -*- coding: utf-8 -*-

import time
import subprocess
import os

#RTC(DS3231) Initialize
def rtc_init():
    dev_check_command = str(subprocess.run(["ls", "/sys/class/i2c-adapter/i2c-1/"], stdout=subprocess.PIPE))
    dc_boolean = "1-0068" in dev_check_command
    if dc_boolean == True:
        print("Device is already initialized.")
    elif dc_boolean == False:
        print("Device is not found on I2C-1. Initialization process will start.")
        os.system("sudo modprobe rtc-ds3232")
        time.sleep(0.5)
        os.system("echo ds3231 0x68 | sudo tee /sys/class/i2c-adapter/i2c-1/new_device > /dev/null")


#RTC(DS3231) Get Time
def rtc_get():
    command = ["sudo", "hwclock", "-r"]
    time_from_rtc = str(subprocess.check_output(command))
    time_simple = time_from_rtc[0:12] + "_" + time_from_rtc[13:15] + time_from_rtc[16:18] + time_from_rtc[19:21]
    return(time_simple.replace("b'",""))


#Network Connection Check
def net_check():
    ping_response = subprocess.run(["ping", "google.co.jp", "-c", "1"], stdout=subprocess.PIPE)
    pr_str = str(ping_response)
    return("ms" in pr_str)


#RTC(DS3231) Set System Time to Device
def rtc_set():
    if net_check() == True:
        subprocess.run(["sudo", "hwclock", "-w"], stdout=subprocess.DEVNULL)
        return("Done.")

    elif net_check() == False:
        return("Network Error occured.")