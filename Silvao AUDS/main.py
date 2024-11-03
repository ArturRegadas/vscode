import customtkinter as ctk
import ttkthemes as ttk
import tkinter as tk
from tkinter.messagebox import askyesno
import beck.beckdomain.adicionarforlistbox as bba
import beck.beckdomain.jane_config01 as janco
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import beck.backresto.junts as junts
import os
import soundcard as sc
import ctypes
import sys

with open("rodar_s_ou_n.txt", "r") as arquivo:
    n=arquivo.read()
if n =="sim":
    def run_as_admin():
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            return False


    if run_as_admin():
        os.system("powershell.exe Install-Module AudioDeviceCmdlets")
def opennotepad():
    os.system("notepad.exe diretorios.txt")

with open("diretorios.txt", "r") as arq:
    teste=arq.read()
    teste=teste.split("\n")
teste_lista_inutil=teste[0].split("    ")
if teste[0]!="":
    if len(teste_lista_inutil[0]) >=2:
        n_lista_teste=""
        for g in range(0,(len(teste_lista_inutil[0])//2)-2):
            n_lista_teste=n_lista_teste+" "
    else:
        n_lista_teste=0

    if len(teste_lista_inutil[2]) >=2:
        d_lista_teste=""
        for g in range(0,(len(teste_lista_inutil[2])//2)-4):
            d_lista_teste=d_lista_teste+" "
    else:
        d_lista_teste=0
else:
    d_lista_teste=0
    n_lista_teste=0





janela=ctk.CTk()

if n == "sim":
    preguntade1o0=askyesno(title="Pedir novamente", message="Você deseja que a solicitação seja pedida novamente?\nPara que o programa funcione é necessario dar permissão de administrador pelo menos 1 vez")
    if not preguntade1o0:
        with open("rodar_s_ou_n.txt", "w") as arquivo:
                    arquivo.write("nao")

janela.title("Silvio Maker")
janela.geometry("290x350")
janela.resizable(False, False)
my_font = ctk.CTkFont(size=30, family="Courier New")

Label1=ctk.CTkLabel(janela, text="Silvão AUDS", font=my_font)
Label1.place(x=15, y=8)

butonimg=tk.PhotoImage(file='Design sem nome (10).png')
button4=tk.Button(janela, image=butonimg, relief='flat', command=janco.configurar)
button4.place(x=229, y=5, height=40, width=40)


list_inutil=tk.Listbox(janela, bg="slategray4",highlightthickness = 0, bd = 0,)
list_inutil.place(x=15, y=10+40, width=250, height=15)
if teste[0]=="":
    list_inutil.insert(0, "   NOME                        TECLA                        DIRETORIO")
else:
    list_inutil.insert(0, f"{n_lista_teste}NOME{n_lista_teste}TECLA{d_lista_teste}DIRETÓRIO")
    

def apagar_da_lista():
    preguntade1o0=askyesno(title="confirmação", message="Você tem certeza?")
    if preguntade1o0:
        apagar=list_audios.delete(tk.ANCHOR)
        with open("diretorios.txt", "w") as arquivo:
            for i in range(1,len(teste)):
                if i!=apagar:
                    arquivo.write(teste[i]+"\n")
def editar_lista():
    
    def botaactedit():
        preguntadetof=askyesno(title="confirmação", message="Você tem certeza?")
        if preguntadetof:
            with open("diretorios.txt", "r") as arq:
                teste=arq.read()
                teste=teste.split("\n")
            selecao=list_audios.get(tk.ACTIVE)
            selecao=teste.index(selecao)
            var_cobobo=cobobo.get()
            ijij=entada_edit.get()
            janela_selcao_editar.destroy()
            nteste=teste[selecao].split("    ")

            if var_cobobo=="Nome":
                list_audios.insert(selecao,f"{ijij}    {nteste[1]}    {nteste[2]}")
                list_audios.delete(selecao+1)
            elif var_cobobo=="Tecla":
                list_audios.insert(selecao,f"{nteste[0]}    {ijij}    {nteste[2]}")
                list_audios.delete(selecao+1)
            elif var_cobobo=="Diretorio":
                list_audios.insert(selecao,f"{nteste[0]}    {nteste[1]}    {ijij}")
                list_audios.delete(selecao+1)
            else:
                messagebox.showerror(title="ERROR", message="Você não escolheu uma opção válida")
            with open("diretorios.txt", "w") as arquivo:
                for i in range(0,len(teste)):
                    if i!=selecao:
                        arquivo.write(teste[i])
                    else:
                        if var_cobobo=="Nome":
                            arquivo.write(f"{ijij}    {nteste[1]}    {nteste[2]}")
                        elif var_cobobo=="Tecla":
                            arquivo.write(f"{nteste[1]}    {ijij}    {nteste[2]}")
                        elif var_cobobo=="Diretorio":
                            arquivo.write(f"{nteste[0]}    {nteste[1]}    {ijij}")
                    if i != len(teste)-1:
                        arquivo.write("\n")
                                          


    janela_selcao_editar=ctk.CTk()
    janela_selcao_editar.title("Editar  itens")
    janela_selcao_editar.geometry("200x130")

    janela_selcao_editar.resizable(False, False)


    cobobo= ctk.CTkComboBox(janela_selcao_editar, state="readonly",values=["Nome", "Tecla", "Diretorio"])
    cobobo.set("Escolha")
    cobobo.pack(padx=20, pady=10)

    entada_edit=ctk.CTkEntry(janela_selcao_editar)
    entada_edit.insert(0,"Nova mudança")
    entada_edit.pack()


    botcobobo=ctk.CTkButton(janela_selcao_editar,text="Editar", command=botaactedit)
    botcobobo.pack(padx=20, pady=10)

    janela_selcao_editar.mainloop()

list_audios=tk.Listbox(janela, bg="slategray4",highlightthickness = 0, bd = 0,)
list_audios.place(x=15, y=25+40, width=250, height=200-15)
for i in range(0, len(teste)):
    list_audios.insert(i,teste[i])


scroll_list_audio1=ctk.CTkScrollbar(janela, orientation="vertical", command=list_audios.yview, height=200+9)
scroll_list_audio1.place(x=15+250, y=7+40)
list_audios["yscrollcommand"]=scroll_list_audio1.set

scroll_list_audio2=ctk.CTkScrollbar(janela, orientation="horizontal", command=list_audios.xview, width=258)
scroll_list_audio2.place(x=12, y=210+40)
list_audios["xscrollcommand"]=scroll_list_audio2.set

botaoadd=ctk.CTkButton(janela,text="Add. Audio",width=79, height=10,fg_color="Coral4", command=lambda: bba.thebutton(list_audios))
botaoadd.place(x=200, y=255-1+40)

botaoadd1=ctk.CTkButton(janela,text="Ouvir Audio",width=79, height=10,fg_color="Bisque4", command=lambda: bba.tocaraqueleaudio(list_audios))
botaoadd1.place(x=200, y=278+40)

botaoacomce=ctk.CTkButton(janela,text="INICIAR",width=172, height=45, command=lambda: junts.inifin(janela))
botaoacomce.place(x=15, y=255+40)






botaoaed=ctk.CTkButton(janela,text=" Editar ",width=80, height=10, fg_color="dark green", command=editar_lista)
botaoaed.place(x=15, y=228+40)

botaoare=ctk.CTkButton(janela,text="Apagar",width=80, height=10,fg_color="maroon", command=apagar_da_lista)
botaoare.place(x=15+80+12, y=228+40)

botaoaver=ctk.CTkButton(janela,text="Ver",width=80, height=10,fg_color="Purple4", command=opennotepad)
botaoaver.place(x=15+80*2+12*2, y=228+40)


janela.mainloop()