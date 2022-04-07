n=int(input("Digite un numero entero: "))
a=list(range(1,n))
b=list()
for i in a:
    Elementos=str(input("Digite los elementos: "))
    b.append(Elementos)
print(b)
for i in a:
    n=int(input("Digite el numero:"))
    if n>=0:
        print(a.index(n))
    elif n<0:
        print("\nEl numero que ha digitado es negativo, digite un numero positivo")
        