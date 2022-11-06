print("Introduzca el número a adivinar")
while True:

    numero = input("Introduzca un número entre 0 y 99 incluidos: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
    
        if 0 <= numero <= 99:
            
            break

# PARTE 2
print("Intente adivinar el número elegido")
while True:

    while True:  
        intento = input("Introduzca un número entre 0 y 99 incluidos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            
            if 0 <= intento <= 99:
        
                break

    if intento < numero:
        print("Error, ese no es el número. Usted se ha quedado por debajo.")
    elif intento > numero:
        print("Error, ese no es el número. Usted se ha pasado")
    else:
        print("Enhorabuena!! Usted ha adivinado el numero")
        break

