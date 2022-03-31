Cadena1=input("digite las letras: ")
Cadena2=str(input("digite los numeros: "))

for letra in Cadena1:
    for numero in Cadena2:
        print(f"{letra}{numero}",end=', ')
    
    