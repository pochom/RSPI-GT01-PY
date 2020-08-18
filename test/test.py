# -*- coding: utf-8 -*-

import serial
import time
import RTC
import pathlib
import os
import datetime








"""
ser = serial.Serial('/dev/ttyS0', 9600)
pos_received = []
unique_pos = []

login_id = "root"
login_pw = "..itiss"
capture_data_count = 100
log_dir = "/home/pi/python/RSPI-GT01-PY/log"
criteria = 0.25

#Elite16用のログイン
def login_sm():
    login_done = False
    while login_done != True:
        print("Trying to login")

        ser.write(bytes(login_id+"\n", encoding='utf-8'))
        time.sleep(1)
        ser.write(bytes(login_pw+"\n", encoding='utf-8'))

        while True:
            ser.write(bytes("\n", encoding='utf-8'))
            data = ser.readline().strip().decode('utf-8')
            print(data)
            time.sleep(0.2)


#Test用のログイン
def login_sm():
    print("Trying to login")
    time.sleep(1)
    ser.write(bytes(login_id, encoding='utf-8'))
    data = ser.readline().strip().decode('utf-8')
    print(data)
    time.sleep(1)
    ser.write(bytes(login_pw, encoding='utf-8'))
    data = ser.readline().strip().decode('utf-8')
    print(data)


#Touchscreen Test
def ts_test():
    cnt = 0
    ser.write(bytes("touchscreen_test -m", encoding='utf-8'))
    print("Touchscreen_test started.")
    while cnt < capture_data_count:
        data = ser.readline().strip().decode('utf-8')
        print(data)
        print("Captured data count is " + cnt + 1 + "\n")
        cnt += 1


#Login to Elite
def serial_login():
    #"mon_imx login:のログを待機しつつシリアルログ出力"
    print("Waiting serial log...")
    login_detect = False
    while login_detect != True:
        data = ser.readline().strip().decode('utf-8')
        print(data)
        login_detect = "mon_imx login:" in data
        
    #ログイン、TS Test実行
    else:
        print("mon_imx login is detected.")
        time.sleep(1)
        login_sm()    


#TS-test Main Function
def serial_test():
    ts_test()

if __name__ == '__main__':
    serial_login()
    time.sleep(1)
    ts_test()



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
