n=int(input("Digite un numero entero: "))
a=list(range(1,n))
b=[]
for i in a:
    c=int(input("Digite el numero: "))
    if c<=0:
        c=0
    b.append(c)
print(b,end=' ')
