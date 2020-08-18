import time
import GPIO_Control as GC
from concurrent.futures import ThreadPoolExecutor

#戻り値Trueを返すうどんボイル関数（所要時間４秒）
def boil_udon():
    done = True
    print('  2:うどんを茹でます。')
    time.sleep(2)
    print('  2:うどんが茹であがりました。')
    return done


#戻り値"Hello, world!"と"Neo Universe."を返すめんつゆ関数（所要時間１秒）
def make_tuyu():
    rtn = "Hello, world!"
    rtn2 = "Neo Universe."
    print('  3:ツユをつくります。')
    time.sleep(0.5)
    print('  3:ツユができました。')
    time.sleep(0.5)
    return rtn, rtn2

#LED点滅関数（ポート番号、周期）
def blink_led(x,y):
    GC.led_set(x, 1)
    time.sleep(y)
    GC.led_set(x, 0)
    time.sleep(y)


print('1:うどんを作ります。')
GC.gpio_setup()


"""
プロセスをインデントせずプールに突っ込む方法
この場合、プールに突っ込んだ直後に次の逐次処理が進む。
pool = ThreadPoolExecutor(max_workers=5)
th1 = pool.submit(boil_udon)
th2 = pool.submit(make_tuyu)
tpl = th2.result()
[print(tpl[i]) for i in range(2)]
"""

#プロセスをインデントしてプールに突っ込む方法
#この場合、プールに突っ込んだスレッドがすべて完了するまで次の逐次処理に移行しない
with ThreadPoolExecutor(max_workers=5) as executor:
    th1 = executor.submit(boil_udon)
    th2 = executor.submit(make_tuyu)
    while th1.running() == True:
        blink_led(15, 0.25)
    else :
        print("Boil_udon has been done.")
        
    #変数tplにmake_tuyuの戻り値（タプル型）を代入
    tpl = th2.result()
    #戻り値２つをprint
    [print(tpl[i]) for i in range(2)]



print('5:うどんができました。')
GC.gpio_cleanup()




"""
def pulus(x, y):
    time.sleep(1)
    sums = x + y
    return sums

with ThreadPoolExecutor(max_workers=1) as executor:
    x = range(5)
    y = range(5, 10)
    res = executor.map(pulus, x, y)


print(list(x))
print(list(y))
print(list(res))
"""




"""SEQUENTIAL
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


"""THREADING
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
"""