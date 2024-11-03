def inifin(jna): 
    from tkinter import messagebox
    with open("index_out.txt", "r") as arquivo:
        oarquivoentry=arquivo.read()
        oarquivoentry=oarquivoentry.split(" ")

    with open("finalizar.txt", "r") as arquivo:
        teclafinalizar=arquivo.read()

    with open("index_entry.txt", "r") as arquivo:
        oarquivoout=arquivo.read()
        oarquivoout=oarquivoout.split(" ")

    if teclafinalizar =="":
        teclafinalizar="'"
    
    messagebox.showinfo(title="Aviso", message="Para finalizar o programa aperte {}".format(teclafinalizar))

    import beck.backresto.entry as entry
    import beck.backresto.play as play
    import beck.backresto.saida as saida
    with open("diretorios.txt", "r") as arquivo:
        direct=arquivo.read()
        direct=direct.split("\n")
    
    jna.destroy()

    from pynput.keyboard import Key, Listener, KeyCode
    stop_key = KeyCode(char=teclafinalizar)


    def on_press(key):
        try:
            tecla_p=key.char
            for i in direct:
                i=i.split("    ")
                if i[1] == tecla_p:
                    entry.entr1(oarquivoentry[0])
                    play.playmusic(i[2])
                    saida.saids(oarquivoout[0])
            

        except AttributeError:
            tecla_p=key

    def on_release(key):
        if key == stop_key:
            return False
            
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()