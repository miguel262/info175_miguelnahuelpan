import string
def encrypt(palabra,N):
    abc=string.ascii_lowercase
    np=""
    for i in palabra:
        cont=0
        if i==" ":
            np=np+" "
        for j in abc:
            cont+=1
            if i==j:
                largo=cont+N-1
                if largo>25:
                    largo=largo-26
                np=np+abc[largo]
    return np
fr=str(raw_input("ingrese frase: "))
n=int(raw_input("ingrese numero: "))
np=encrypt(fr,n)
print "su nueva frase es: "+np
   
