
from cgitb import text
from typing import TextIO


Alfabeto=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
Texto=str(input("digite la palabra: "))
contar=0

for i in Texto:
    if Texto in Alfabeto:
        contar+=1        
    else:
        print("Se ha encontrado caracteres No alfabeticos")
        break
if contar==len(Texto):
        print("Todos los caracteres son alfabeticos")        
    