def multiplo(size):
    lista=[]
    while size>0:
        if size%3==0 and size%7==0:
            lista.append(size)
            
        size=size-1
    print lista
multiplo(84)
