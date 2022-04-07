from tkinter import N


n=int(input("Digite un numero entero: "))
a=list(range(1,n))
b=list()
for i in a:
    Elementos=int(input("Digite los elementos: "))
    b.append(Elementos)
print(b)

for j in b:
    n=int(input("digite el numero: "))
    if n>=0:
        print(b.index(n))    
    elif n<0:
        print("\nEl numero que ha digitado es negativo, digite un numero positivo")