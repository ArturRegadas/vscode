import customtkinter as ctk
import tkinter as tk
import soundcard as sc
from tkinter import messagebox
import sys


def listar():
    list_c_auds=[]
    input_devices = sc.all_microphones()
    for i, device in enumerate(input_devices):
        list_c_auds.append(f"0  {device}")

    output_devices = sc.all_speakers()
    for i, device in enumerate(output_devices):
        list_c_auds.append(f"1  {device}")
    c=1
    x=[]
    for i in list_c_auds:
        l=i.split("  ")
        if l[0] == "1":
            c+=1
    for i in list_c_auds:
        l=i.split("  ")
        if l[0] == "0":
            x.append(f"{c} {l[1]}")
            c+=1
    return x



def configurar():
    with open("finalizar.txt", "r") as arquivo:
        entryfin=arquivo.read()

    with open("rodar_s_ou_n.txt", "r") as arquivo:
        checkfin=arquivo.read()
    count=1
    alistaempy=listar()
    janela_da_config=ctk.CTk()

    janela_da_config.title("Configurar Programa")
    janela_da_config.geometry("300x150")
    janela_da_config.resizable(False, False)

    estado=ctk.StringVar()
    check=ctk.CTkCheckBox(janela_da_config, text="Pedir Permissão?",variable=estado, onvalue="sim", offvalue="nao")
    check.place(x=0, y=1)
    if checkfin == "sim":
        check.select(1)



    entry=ctk.CTkEntry(janela_da_config)
    entry.place(x=150, y=1)
    if entryfin =="":
        entry.insert(0, "Tecla finalizar")
    else:
        entry.insert(0, entryfin)

    listacomtudo=tk.Listbox(janela_da_config, relief="flat", bg="slategray4",highlightthickness = 0, bd = 0)
    listacomtudo.place(x=5,y=35, height=80, width=290-15)
    def pegarmic():
        try:
            with open("index_entry.txt", "w") as arquivo:
                arquivo.write(listacomtudo.get(tk.ACTIVE))
        except:
            messagebox.showerror(title="ERROE", message="Selecione uma entrada de audio")
    def pegarmixagem():
        try:
            with open("index_out.txt", "w") as arquivo:
                arquivo.write(listacomtudo.get(tk.ACTIVE))
        except:
            messagebox.showerror(title="ERROR", message="Selecione sua saida de audio")


    scroll_list_audio12=ctk.CTkScrollbar(janela_da_config, orientation="vertical", command=listacomtudo.yview, height=80)
    scroll_list_audio12.place(x=290-15, y=35)
    listacomtudo["yscrollcommand"]=scroll_list_audio12.set
    listacomtudo.insert(0, "ENTRADAS DE AUDIO: ")

    def alterar():
        with open("rodar_s_ou_n.txt", "w") as arquivo:
            arquivo.write(check.get())
        n=entry.get()        
        if len(n) ==1:
            with open("finalizar.txt", "w") as arquivo:
                arquivo.write(n)
            messagebox.showinfo(title="Alterações", message="Todas as alterações ocorreram bem")
        else:
            messagebox.showerror(title="ERROR", message="Insira uma tecla valia")
            messagebox.showinfo(title="Alterações", message="Alguma alterações não puderam ocorrer")

        janela_da_config.destroy()
    for i in range(0, len(alistaempy)):
        listacomtudo.insert(i+1, alistaempy[i])
    Botaoentrada=ctk.CTkButton(janela_da_config, text="Definir Microfone", width=10, command=pegarmic)
    Botaoentrada.place(x=5, y=35+82)

    Botaoesaida=ctk.CTkButton(janela_da_config, text="Definir Mixagem", width=10, command=pegarmixagem)
    Botaoesaida.place(x=125, y=35+82)

    Botaoealt=ctk.CTkButton(janela_da_config, text="Alterar", width=10, command=alterar)
    Botaoealt.place(x=240, y=35+82)


    janela_da_config.mainloop()