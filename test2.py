# -*- coding: utf-8 -*-

import serial
import time
import RTC
import pathlib
import os
import datetime

ser = serial.Serial('/dev/ttyS0', 9600)
ser_timeout = serial.Serial('/dev/ttyS0', 9600, timeout=0.1)
pos_received = []
unique_pos = []

login_id = "root"
login_pw = "..itiss"
capture_data_count = 100
log_dir = "/home/pi/python/RSPI-GT01-PY/log"
criteria = 0.25

#Elite16用のログイン
def login_sm():
    print("Trying to login")
    ser.write(bytes(login_id, encoding='utf-8'))
    ser.write(bytes("\n", encoding='utf-8'))
    time.sleep(1)
    ser.write(bytes(login_pw, encoding='utf-8'))
    ser.write(bytes("\n", encoding='utf-8'))

    ser.reset_input_buffer()
    [ser.write(bytes("\n", encoding='utf-8')) for i in range(2)]

    data = []
    cnt = 10
    for i in range(cnt):
        data.append(ser_timeout.readline().strip().decode('utf-8'))
        print("log" + str(i) + ": " + data[i])
    ser.reset_input_buffer()
    for i in range(cnt):
        if "root@" in data[i]:
            print ("Logged in.")
            break


if __name__ == '__main__':
    login_sm()
    time.sleep(1)
    ser.write(bytes("exit", encoding='utf-8'))
    ser.write(bytes("\n", encoding='utf-8'))
    print("Logged out")

"""
log_dir = "/home/pi/python/RSPI-GT01-PY/log"

#log_dirディレクトリの存在確認後、無ければ作成
os.makedirs(log_dir, exist_ok=True)

#現在日時取得
current_datetime = str(datetime.datetime.now())[0:10] + "_" + str(datetime.datetime.now())[11:19]

#ファイル名代入、ファイルパス設定
file_name = "Test_Report_" + current_datetime + ".log"
file_path = pathlib.Path(log_dir + "/" + file_name)
print(file_path)
file_path.touch(exist_ok=False)



test_report_header = []
test_report_header.append("Elite16v2 On-wing Test Report")
test_report_header.append("Judgement Formula: X = A / B")
trh = "\n".join(test_report_header)

test_report = ["0:110","10:1100","1030:3039","2020:10192","3003:1012"]
tr = "\n".join(test_report)

with open(file_path, 'w') as f:
    f.write(trh)
    f.write(tr)
"""
