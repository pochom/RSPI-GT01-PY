# -*- coding: utf-8 -*-

import tkinter as tk
import Serial_Control as SC
import GPIO_Control as GC
import RTC
import time
import elite16v2GTTT1_support as sp

log_dir = "/home/pi/python/RSPI-GT01-PY/GUI_Edition/log"

#Applicationという名前のクラスをtkinter.Frameを継承して生成
class Application(tk.Frame):
    #Applicationクラスのコンストラクタ(初期化時実行メソッド)を定義
    def __init__(self, master=None):
        #スーパークラス(tk.Frame)の__init__()メソッドを呼び出し
        super().__init__(master)
        #スーパークラスの.title, .geometryアトリビュートに情報付与
        master.geometry("600x150+650+400")
        master.resizable(0, 0)
        master.title("Elite16v2 GT Test Tool GUI Edition (Ver:0.01)")
        master.configure(highlightcolor="black")
        self.pack()


        #1段目
        self.lbl_led1 = tk.Label()
        self.lbl_led1.place(x=600*0.05, y=150*0.17)
        self.lbl_led1.configure(text='''LED1(Init):''')

        self.led1 = tk.Label()
        self.led1.place(x=600*0.18, y=150*0.11)
        self.led1.configure(text="●", foreground="#FF0", font=("",20))

        self.lbl_led2 = tk.Label()
        self.lbl_led2.place(x=600*0.27, y=150*0.17)
        self.lbl_led2.configure(text='''LED2(Noise):''')

        self.led2 = tk.Label()
        self.led2.place(x=600*0.425, y=150*0.11)
        self.led2.configure(text="●", foreground="#00F", font=("",20))

        self.lbl_led3 = tk.Label()
        self.lbl_led3.place(x=600*0.523, y=150*0.17)
        self.lbl_led3.configure(cursor="fleur")
        self.lbl_led3.configure(text='''LED3(Pass):''')

        self.led3 = tk.Label()
        self.led3.place(x=600*0.67, y=150*0.11)
        self.led3.configure(text="●", foreground="#0F0", font=("",20))

        self.lbl_led4 = tk.Label()
        self.lbl_led4.place(x=600*0.767, y=150*0.17)
        self.lbl_led4.configure(text='''LED4(Fail):''')

        self.led4 = tk.Label()
        self.led4.place(x=600*0.9, y=150*0.11)
        self.led4.configure(text="●", foreground="#F00", font=("",20))


        #2段目
        self.lbl_log = tk.Label()
        self.lbl_log.place(x=600*0.05, y=150*0.42)
        self.lbl_log.configure(text="TEST RESULT: PASS (20%)", font=("",16))

        self.btn_run = tk.Button()
        self.btn_run.place(x=600*0.55, y=150*0.46, height=30, width=60)
        self.btn_run.configure(command=lambda :action_run())
        self.btn_run.configure(text='''Run''')

        self.btn_rst = tk.Button()
        self.btn_rst.place(x=600*0.665, y=150*0.46, height=30, width=60)
        self.btn_rst.configure(command=lambda :action_rst())
        self.btn_rst.configure(text='''Reset''')

        self.btn_od = tk.Button()
        self.btn_od.place(x=600*0.78, y=150*0.46, height=30, width=100)
        self.btn_od.configure(command=lambda :action_od())
        self.btn_od.configure(takefocus="")
        self.btn_od.configure(text='''Open Directly''')


        #3段目
        self.lbl_log = tk.Label()
        self.lbl_log.place(x=600*0.05, y=150*0.733)
        self.lbl_log.configure(text="Log directly")

        self.Entry1 = tk.Entry()
        self.Entry1.place(x=600*0.2, y=150*0.73,height=24, relwidth=0.75)
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="fleur")
        self.Entry1.insert(tk.END, log_dir)


        #ボタン押下時アクション関数定義
        def action_run():
            #print("Run")
            #GC.gpio_setup()
            self.led1.configure(foreground="#FFF", font=("",20))
            #GC.led_set(15,0)
            time.sleep(0.5)
            self.led1.configure(foreground="#FF0", font=("",20))
            #GC.led_set(1,1)
            time.sleep(0.5)


        def action_rst():
            print("Reset")

        def action_od():
            print("Open Directly")


#tkinter.Tk(): ルートウィンドウ生成
root = tk.Tk()

#Applicationクラスのインスタンス生成
#masterはウィジットの配置先、この場合rootを指定
app = Application(master=root)
#メイン処理実行
app.mainloop()