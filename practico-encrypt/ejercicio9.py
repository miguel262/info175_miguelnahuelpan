def cenit_polar(palabra):
    np=""
    for i in palabra:
        if i=="c" or i=="e" or i=="n" or i=="i" or i=="t":
            np=np+i.replace("c","p").replace("e","o").replace("n","l").replace("i","a").replace("t","r")
        elif i=="p" or i=="o" or i=="l" or i=="a" or i=="r":
            np=np+i.replace("p","c").replace("o","e").replace("l","n").replace("a","i").replace("r","t")
        else:
            np=np+i
    return np
nfr=cenit_polar("cenit polar")
print ("la nueva palabra es: "+nfr)
