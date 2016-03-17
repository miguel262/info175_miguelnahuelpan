def Numeros():
  x=input("ingrese un numero: ")
  y=input("ingrese un numero: ")
  resultado=""
  if(x==y):
      resultado="iguales"
      return resultado
  elif(x>y):
      resultado="el mayor es: "+str(x)
      return resultado
  else:
      resultado="el mayor es: "+str(y)
      return resultado
print Numeros()
