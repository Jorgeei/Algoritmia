'Escriba un programa en Python que acepte 3 números y calcule el mínimo'
num_1=7
num_2=4
num_3=9

if num_1 < num_2:
    if num_1 < num_3:
        minimo_valor = num_1
    else:
        minimo_valor = num_3
elif num_2 < num_3:
    minimo_valor = num_2
else:
    minimo_valor = num_3

print(minimo_valor)