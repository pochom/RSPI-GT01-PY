# -*- coding: utf-8 -*-

import pathlib
import os
import RTC

log_dir = "/home/pi/python/RSPI-GT01-PY/log"

#log_dirディレクトリの存在確認後、無ければ作成
os.makedirs(log_dir, exist_ok=True)

#現在日時取得
current_datetime = RTC.rtc_get()

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

