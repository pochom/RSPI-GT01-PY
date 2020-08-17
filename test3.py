import time
import threading

def boil_udon():
  print('  2:うどんを茹でます。')
  time.sleep(2)
  print('  2:うどんが茹であがりました。')
  time.sleep(2)

def make_tuyu():
  print('  3:ツユをつくります。')
  time.sleep(0.5)
  print('  3:ツユができました。')
  time.sleep(0.5)
"""
print('1:うどんを作ります。')
time.sleep(2)
boil_udon()
time.sleep(2)
make_tuyu()
time.sleep(2)
print('4:盛り付けます。')
time.sleep(2)
print('5:うどんができました。')
"""
print("########")

print('1:うどんを作ります。')
time.sleep(2)
#スレッド処理の定義
thread1 = threading.Thread(target=boil_udon)
thread2 = threading.Thread(target=make_tuyu)
#スレッド処理開始
thread1.start()
thread2.start()
#スレッド完了まで待機(これがないとstartした処理がひとつでも完了したら盛り付けされる)
thread1.join()
thread2.join()
print('4:盛り付けます。')
time.sleep(2)
print('5:うどんができました。')