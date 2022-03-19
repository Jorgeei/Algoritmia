e_final=float(input("digite nota de evaluacion: "))
quiz_1=float(input("digite nota del quiz_1: "))
quiz_2=float(input("digite nota del quiz_2: "))
quiz_3=float(input("digite nota del quiz_3: "))
trabajo_final=float(input("digite nota de trabajo final: "))

nota_final=(e_final*0.50)+(((quiz_1+quiz_2+quiz_3)/3)*0.20)+(trabajo_final*0.30)
print(f'la nota final del estudiante pepito perez es: {nota_final:.2f}')
