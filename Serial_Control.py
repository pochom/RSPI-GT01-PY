# -*- coding: utf-8 -*-

import serial
import time
import RTC
import pathlib
import os
import datetime
import GPIO_Control as GC

ser = serial.Serial('/dev/ttyS0', 9600)
ser_timeout = serial.Serial('/dev/ttyS0', 9600, timeout=0.1)
pos_received_global = []
unique_pos_global = []

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
    [ser.write(bytes("\n", encoding='utf-8')) for i in range(5)]

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


#Login to Elite
def serial_login():
    #"mon_imx login:のログを待機しつつシリアルログ出力"
    print("Waiting serial log...")
    login_detect = False
    while login_detect != True:
        try:
            data = ser.readline().strip().decode('utf-8')
        #Elite電源投入時のノイズに対する例外処理
        except UnicodeDecodeError:
            ser.reset_input_buffer()
            data = ""
        print(data)
        login_detect = "mon_imx login:" in data

    #ログイン、TS Test実行
    else:
        login_sm()    


#TS-test Main Function
def serial_test():
    #Variable init
    pos_received = pos_received_global
    unique_pos = unique_pos_global

    #Touchscreen Test
    ser.write(bytes("touchscreen_test -m", encoding='utf-8'))
    ser.write(bytes("\n", encoding='utf-8'))
    #ノイズ印加開始
    GC.ngen_set(1)
    print("Touchscreen_test started.")
    #data = ser.readline().strip().decode('utf-8')
    #print(data)

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
       
    else:
        #ノイズ印加停止
        GC.ngen_set(0)
        #リストに格納した値を一括出力
        #Unique座標をリストに代入
        pos_extracted_list = []
        for i in range(capture_data_count):
            if unique_pos.count(pos_received[i]) == 0:
                unique_pos.append(pos_received[i])
                pos_extracted_list.append(str(i + 1) + ": " + pos_received[i] + " [X]")
            else:
                pos_extracted_list.append(str(i + 1) + ": " + pos_received[i] + " [ ]")
            print(pos_extracted_list[i])
    
    #返り値計算
    result_a = len(pos_received)
    result_b = len(unique_pos)
    result_x = '{:.2f}'.format(len(unique_pos) / len(pos_received) * 100)

    #テストレポート出力
    #log_dirディレクトリの存在確認後、無ければ作成
    os.makedirs(log_dir, exist_ok=True)

    #現在日時取得
    #current_datetime = RTC.rtc_get()
    current_datetime = str(datetime.datetime.now())[0:10] + "_" + str(datetime.datetime.now())[11:19]

    #ファイル名代入、ファイルパス設定
    file_name = "Test_Report_" + current_datetime + ".log"
    file_path = pathlib.Path(log_dir + "/" + file_name)
    print("Test report is successfully generated as " + str(file_path))
    file_path.touch(exist_ok=False)

    #テストレポートヘッダ部作成
    test_report_header = []
    test_report_header.append("Elite16v2 On-wing Test Report")
    test_report_header.append("Judgement Formula: X = A / B")
    test_report_header.append("Judgement Criteria: " + str(criteria * 100) + "%")
    test_report_header.append("DATA A: " + str(result_a))
    test_report_header.append("DATA B: " + str(result_b))
    test_report_header.append("DATA X: " + str(result_x) + "%")
    
    #PASS/FAIL判定行追加
    if float(result_x) < criteria * 100 :
        test_report_header.append("RESULT: PASS")
        test_report_header.append("\n")
        
    else:
        test_report_header.append("RESULT: FAIL")
        test_report_header.append("\n")

    #改行コード追加
    trh = "\n".join(test_report_header)
    tr = "\n".join(pos_extracted_list)

    #テストレポートに書き込み
    with open(file_path, 'w') as tr_write:
        tr_write.write(trh)
        tr_write.write(tr)

    criteria_return = criteria

    return result_a, result_b, result_x, criteria_return

