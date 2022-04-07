a=["Lunes",24.5,"Martes",65,"Miercoles",True,"Jueves",88.9,"Viernes",99.9,"Agua",False,"Sol",33,"Tierra",105.6,"Fuego",44,"Aire",789.7,"Limón"]
print(a)
for i in a:
    n=int(input("igrese un numero entero: "))
    if n>=0:
        print(a[n])
    elif n<=0:
        print("\nDigite un numero positivo")
