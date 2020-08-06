# -*- coding: utf-8 -*-

import serial
import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
pos_received = []

login_id = "root"
login_pw = "pasuwa-do"
capture_data_count = 100


#Elite16用のログイン
"""
def login_sm():
    while True:
        ser.write(login_id)
        res = "Password:" in ser.readline().decode('utf-8')
        if res == True:
            time.sleep(1)
            ser.write(login_pw)
        elif res == False:
            time.sleep(1)
"""


#Test用のログイン
def login_sm():
    ser.write(bytes(login_id, encoding='utf-8'))
    time.sleep(0.5)
    ser.write(bytes(login_pw, encoding='utf-8'))


#Touchscreen Test
def ts_test():
    ser.write(bytes("TOUCHSCREEN_TEST -M", encoding='utf-8'))


def serial_test():
    #"mon_imx login:のログを待機しつつシリアルログ出力"
    login_detect = False
    while login_detect != True:
        data = ser.readline().strip().decode('utf-8')
        print(data)
        login_detect = "mon_imx login:" in data

    #ログイン、TS Test実行
    else:
        login_sm()
        time.sleep(0.25)
        ts_test()

        #取得座標数が指定値に達するまでリストに代入し続ける
        while len(pos_received) < capture_data_count:
            ts_data = ser.readline().strip().decode('utf-8')
            pos_boolean = "[1]" in ts_data

            #座標を含むログから座標部分を抽出しリストに代入
            if pos_boolean == True:
                pos_start = ts_data.find("[1][") + 4
                pos_end = ts_data.find("]", pos_start)
                pos_extracted = ts_data[pos_start:pos_end]
                pos_received.append(pos_extracted)
    
        #リストに格納した値を一括出力
        else:
            for i in range(capture_data_count):
                print(str(i + 1) + ":" + pos_received[i])


serial_test()
print("Data numbers in the list is")
print(len(pos_received))
print("Position data was correctly captured!!!")