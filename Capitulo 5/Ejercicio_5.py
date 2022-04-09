n=int(input("digite el numero entero:"))
a=list(range(1,n))
b=[]

for i in a:
    c=str(input("digite la palabra: "))
    b.append(c.upper())
print(list(set(b)))