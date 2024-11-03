from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
import customtkinter as cct
import tkinter as tk
from tkinter import messagebox
import beck.backresto.play as bc
def tocaraqueleaudio(alista):
    alista=alista.get(tk.ACTIVE)
    alista=alista.split("    ")
    alista=alista[2]
    if "\n" in alista:
        alista=alista[:alista.index("\n")]
    bc.playmusic(alista)

def addddd (arquivocomputer, teclaatribuida1, lista_audios):
    with open("diretorios.txt", "r") as arquivo:
        diretorio_var=arquivo.read()
        diretorio_var=diretorio_var.split("\n")
    nome_do_arquivo=arquivocomputer.split("/")
    nome_do_arquivo=nome_do_arquivo[len(nome_do_arquivo)-1]
    nome_do_arquivo=nome_do_arquivo[:nome_do_arquivo.index(".wav")]
    lista_audios.insert(len(diretorio_var)-1,f"{nome_do_arquivo}    {teclaatribuida1}    {arquivocomputer}\n")
    with open("diretorios.txt", "a") as arquivo:
        if diretorio_var!=[""]:
            arquivo.write("\n")
        arquivo.write(f"{nome_do_arquivo}    {teclaatribuida1}    {arquivocomputer}")



def thebutton(lista_audios):

    def cert():
        preguntade1o0=askyesno(title="confirmação", message="Voce tem certeza?\nCaso já tenha um audio vinculado a essa tecla, o audio nao funcionará\nPosteriormente será possivel mudar a tecla selecionada")
        if preguntade1o0:
            teclaatribuida=tecla21.get()
            janela_tecla.destroy()
            addddd(arquivocomputer, teclaatribuida, lista_audios)
    arquivocomputer=askopenfilename(title="Selecione um arquivo .wav")
    if arquivocomputer!="":
        if arquivocomputer[len(arquivocomputer)-4:]!=".wav" and arquivocomputer[len(arquivocomputer)-4:]!=".WAV":
            messagebox.showerror(title="ERROR", message="Voce não selecionou um arquivo válido\nou não selecionou um arquivo")
        else:
            janela_tecla=cct.CTk()
            janela_tecla.title("Selecione uma tecla para usar esse audio")
            janela_tecla.geometry("163x92")
            janela_tecla.resizable(False, False)

            tecla21=cct.CTkEntry(janela_tecla)
            tecla21.insert(0, "Insira a tecla")
            tecla21.place(x=11, y=11)

            botao21=cct.CTkButton(janela_tecla, command=cert)
            botao21.place(x=11, y=45)

            def clique(retorno):
                print(f'x:{retorno.x} / y : {retorno.y} geo :{janela_tecla.geometry()}')
            janela_tecla.bind('<Button-3>', clique)

            janela_tecla.mainloop()
    else:
        messagebox.showerror(title="ERROR", message="Voce não selecionou um arquivo válido\nou não selecionou um arquivo")