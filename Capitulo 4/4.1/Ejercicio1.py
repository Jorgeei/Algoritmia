'''Escriba un programa en Python que acepte la opción de dos jugadoras en
Piedra-Papel-Tijera y decida el resultado'''

jugador1=input('digite la opcion del jugador1: ')
jugador2=input('digite la opcion del jugador2: ')

if jugador1==jugador2:
    resultado= 'Empate'
    ganador=0
elif jugador1=='piedra' and jugador2=='tijera':
    resultado='La piedra aplasta la tijera'
    ganador=1
elif jugador1 =='tijera' and jugador2 == 'piedra':
    resultado='La piedra aplasta la tijera'
    ganador=2
elif jugador1=='tijera' and jugador2=='papel':
    resultado='La tijera corta el papel'
    ganador=1
elif jugador1=='papel' and jugador2=='tijera':
    msg = 'La tijera corta el papel'
    winner =2
elif jugador1=='papel' and jugador2=='piedra':
    resultado='El papel envuelve la piedra'
    ganador=1
elif jugador1=='piedra' and jugador2=='papel':
    resultado='El papel envuelve la piedra'
    ganador=2

if resultado==0:
    ganador='Empate'
else:
    resultado= f'Gana persona{ganador}: {resultado}'

print(resultado)

