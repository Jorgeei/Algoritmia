jug_1=input("digite la opcion del jug_1: ")
jug_2=input("digite la opcion del jug_2: ")

if jug_1==jug_2:
    print(f"los jugadores han empatado")
    
elif jug_1=="papel" and jug_2=="piedra":
    print("¡Gana! jug_1: el papel envuelve la piedra")
    
elif jug_1=="papel" and jug_2=="tijera":
    print("¡Gana! el jug_2: la tijera corta papel")
    
elif jug_1=="piedra" and jug_2=="tijera":
    print("¡Gana! jug_1: la piedra aplasta la tijera")
    
elif jug_1=="piedra" and jug_2=="papel":
    print("¡Gana! jug_2: el papel en vuelve la piedra")
    
elif jug_1=="tijera" and jug_2=="papel":
    print("¡Gana! jug_1 tijera corta papel")
    
elif jug_1=="papel" and jug_2=="tijera":
    print("!Gana¡ jug_2 corta papel")  
    
elif jug_1=="papel" and jug_2=="piedra":
    print("¡Gana! jug_1 piedra emvuelve papel")
    
elif jug_1=="papel" and jug_2=="tijera":
    print("!Gana¡ jug_2 tijera corta papel")
    
elif jug_1=="papel" and jug_2=="tijera":
    print("¡Gana! jug_2 tijera corta papel")
else:
    print("¡Vamos que se puede ganar!")
    