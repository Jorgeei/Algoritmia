volar=bool(int(input("¿Puede Volar?: ")))
humano=bool(int(input("¿Es humano: ")))
mascara=bool(int(input("¿Tiene mascara?: ")))

if volar==True and humano==True and mascara==True:
    print("iroman")
elif volar==True and humano==True and mascara==False:
    print("capitan marvel")
elif volar==True and humano==False and mascara==True:
    print("ronan accuser") 
elif volar==True and humano==False and mascara==True:
    print("vision")
elif volar==False and humano==True and mascara==True:
    print("spiderman")
elif volar==False and humano==True and mascara==False:
    print("hulk")
elif volar==False and humano==False and mascara==True:
    print("black bolt")
elif volar==False and humano==False and mascara==False:
    print("thanos")
else:
    print("Ninguno es Super_Heroe")
    