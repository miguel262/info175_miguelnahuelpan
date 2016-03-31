from Tkinter import *
import string
def cesar(palabra,n):
    numero = int(n)
    abc=string.ascii_lowercase
    np=""
    for i in palabra:
        cont=0
        if i==" ":
            np=np+" "
        for j in abc:
            cont+=1
            if i==j:
                largo=cont+numero-1
                if largo>25:
                    largo=largo-26
                np=np+abc[largo]
    salida.insert(INSERT, np +"\n")
  
    return np

def cenit_polar(palabra):
    np=""
    for i in palabra:
        if i=="c" or i=="e" or i=="n" or i=="i" or i=="t":
            np=np+i.replace("c","p").replace("e","o").replace("n","l").replace("i","a").replace("t","r")
        elif i=="p" or i=="o" or i=="l" or i=="a" or i=="r":
            np=np+i.replace("p","c").replace("o","e").replace("l","n").replace("a","i").replace("r","t")
        else:
            np=np+i
    salida.insert(INSERT, np +"\n")
    return np

def encryptar():
    if opcion.get()==1:
        cenit_polar(palabraCaja.get())
    elif opcion.get()==2:
        cesar(palabraCaja.get(),numeroCaja.get())

ventana=Tk()
opcion=IntVar()
ventana.geometry("500x200")
frame = Frame(ventana)
frame.pack()
bottomframe = Frame(ventana)
bottomframe.pack(side=BOTTOM)
etiq1=Label(frame,text="ingrese frase")
etiq1.pack()
palabraCaja=Entry(frame,width=60)
palabraCaja.pack()
etiq2=Label(frame,text="modo de encriptacion")
etiq2.pack()
boton1=Radiobutton(frame,text="cenit-polar",value=1,variable=opcion)
boton1.pack(side=LEFT)
boton2=Radiobutton(frame,text="cesar",value=2,variable=opcion)
boton2.pack(side=LEFT)
etiq3=Label(bottomframe,text="numero de saltos")
etiq3.pack()
numeroCaja=Entry(bottomframe)
numeroCaja.pack()
boton3=Button(bottomframe,text="Encriptar",command=encryptar)
boton3.pack()
salida = Text(bottomframe,height=5, width=60)
salida.pack(side=BOTTOM)
ventana.mainloop()
