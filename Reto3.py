import numpy as np
import random
from math import sqrt
def encriptado(texto):
  desordenado=[]
  clave=[]
  codigo_unicode=[]
  texto=input("Inserte su mensaje: ")
  medida_texto=len(texto)
  n=sqrt(medida_texto)
  if (n//1)!=n:
    n=(n//1)+1

  n=int(n)

  for i in range(len(texto),n*n):
    texto=texto+"_"

  texto=list(texto)

  for i in range(len(texto)):
    clave.append(i)

  random.shuffle(clave)

  for i in clave:
    desordenado.append(texto[i])

  matriz1 = np.array(desordenado).reshape(n,n)

  for i in desordenado:
    v=ord(i)
    codigo_unicode.append(v)

  array_final = np.array(codigo_unicode).reshape(n,n)

  codigo_desencriptado=[]
  texto=[]
  for i in codigo_unicode:
    k=chr(i)
    codigo_desencriptado.append(k)

  for i in range(len(codigo_desencriptado)):
    posicion=clave.index(i)
    texto.append(codigo_desencriptado[posicion])
  
  nombre="".join(texto)
  nombre=nombre.replace("_","")
  print(codigo_desencriptado)
  print(clave)
  print(texto)
  print(nombre)
