from tkinter import ttk, PhotoImage, IntVar,  LabelFrame
import tkinter as th
from ttkthemes import ThemedTk
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
x=0

#comandos


lg = "user"
password = "123"



#criação da janela
janela=ThemedTk(theme='breeze')
janela.title('autoclicker')
janela.geometry('1280x720')






def login():
    usuario=entry1.get()
    usuario=str(usuario)
    senha=entry2.get()
    senha=str(senha)
    concordo=estado.get()

    def comecar():
        cps = radio.get()
        estartar=entrada.get()
        estartar=str(estartar)
        mouse=combo.get()
        mouse=str(mouse)
        encerrar=entrada1.get()
        encerrar=str(encerrar)
        if estartar == '' or len(estartar) > 1 or estartar == ' ':
            labelerro1=ttk.Label(janela_1, text='você nao preecheu ou preecheu alguma das informações', foreground='#ce0018')
            labelerro1.place(x=85, y=122)

        elif encerrar == '' or len(encerrar) > 1 or encerrar == ' ':
            labelerro2=ttk.Label(janela_1, text='você nao preecheu ou preecheu alguma das informações', foreground='#ce0018')
            labelerro2.place(x=85, y=122)
        else:
            janela_1.destroy()
            if cps == 0:
                delay = 0.05
            if cps == 1:
                delay = 0.032
            if cps == 2:
                delay = 0.01
            if mouse == 'esquerdo':
                button= Button.left
            else:
                button= Button.right

            start_stop_key = KeyCode(char=estartar)
            exit_key = KeyCode(char=encerrar)

            class ClickMouse(threading.Thread):
                def __init__(self, delay, button):
                    super(ClickMouse, self).__init__()
                    self.delay = delay
                    self.button = button
                    self.running = False
                    self.program_run = True

                def start_clicking(self):
                    self.running = True

                def stop_clicking(self):
                    self.running = False

                def exit(self):
                    self.stop_clicking()
                    self.program_run = False

                def run(self):
                    while self.program_run:
                        while self.running:
                            mouse.click(self.button)
                            time.sleep(self.delay)
                        time.sleep(0)

            mouse = Controller()
            thread = ClickMouse(delay, button)
            thread.start()

            def on_press(key):
                if key == start_stop_key:
                    if thread.running:
                        thread.stop_clicking()
                    else:
                        thread.start_clicking()
                elif key == exit_key:
                    thread.exit()
                    listener.stop()

            with Listener(on_press=on_press) as listener:
                listener.join()


    if usuario == lg and senha == password and concordo == 1:
        janela.destroy()
        # criação da janela
        janela_1=ThemedTk(theme='breeze')
        janela_1.geometry('500x191')
        janela_1.resizable(False, False)
        # fundo

        label1=LabelFrame(janela_1, text='Cliques por segundo (cps)', font='Arial 10' )
        label1.place(x=11, y=10, width=250, height=50)

        radio=IntVar()

        radio1=ttk.Radiobutton(janela_1, text=15,  value=0, variable=radio)
        radio1.place(x=29-5, y= 28)

        radio2=ttk.Radiobutton(janela_1, text=30,  value=1,variable=radio)
        radio2.place(x=110, y= 28)

        radio3=ttk.Radiobutton(janela_1, text=60,  value=2, variable=radio)
        radio3.place(x=200, y= 28)





        label2 = ttk.Label(janela_1, text='tecla para iniciar / pausar', font='Arial 11')
        label2.place(x=265, y=15, width=250, height=50)

        entrada=ttk.Entry(janela_1)
        entrada.place(x=440, y= 26, width=50, height=28)

        label3=ttk.LabelFrame(janela_1, text='Botão do mouse')
        label3.place(x=11, y=75, width=113 , height=45)

        combo = ttk.Combobox(janela_1)
        combo['values'] = ('esquerdo', 'direito')
        combo.current(0)
        combo.place(x=19, y=90, width=98, height=27)
        combo["state"] = "readonly"

        label4=ttk.Label(janela_1, text='tecla para encerrar programa', font='Arial 11')
        label4.place(x=135, y= 90)

        entrada1=ttk.Entry(janela_1)
        entrada1.place(x=332, y=85, width=50, height=28)

        button3=ttk.Button(janela_1,text='SAIR' ,command=janela_1.destroy)
        button3.place(x=410, y=85, width=60, height=28)

        butonimg=PhotoImage(file='comecar.png')
        button4=th.Button(janela_1, image=butonimg, relief='flat', command=comecar)
        button4.place(x=175, y=145, width=150, height=40)



        janela_1.mainloop()




    else:
        labelerro=ttk.Label(janela, text='Alguma das as informações a cima estão erradas, ou não estão preenchidas', background='#ededed',foreground='#ce0018')
        labelerro.place(x=760, y=511)

#fundo
pngl= PhotoImage(file='definitivo.png')
labelpng=ttk.Label(janela, image=pngl)
labelpng.pack()
labelpng.place(x=0, y=0)

#entrys
entry1=ttk.Entry(janela, font='ProximaNova 21', background='#ededed')
entry1.insert(0, "User@email.com")
entry1.place(x=759, y=265, width=434, height=49)

entry2=ttk.Entry(janela, font='ProximaNova 21', background='#ededed', show='*')
entry2.insert(0, 'password')
entry2.place(x=759, y=413, width=434, height=49)

#checkbutton
estado=IntVar()
checkb1=ttk.Checkbutton(janela, text="", var=estado, onvalue=1, offvalue=0)
checkb1.place(x=1080, y=486, width=30, height=30)
estado.set(0)

#buttons
pngb1=PhotoImage(file='Entrar.png')
button1=th.Button(janela, image=pngb1,relief="flat",  command=login)
button1.place(x=852, y= 563, width=247, height=55)

button2=th.Button(janela, text='termos', relief='flat')
button2.place(x=1220, y=661, width=45, height=15)

button5=th.Button(janela, text='sair', command=janela.destroy, relief='flat')
button5.place(x=660, y=661, width=45,height=15)



#saber a posição



janela.mainloop()