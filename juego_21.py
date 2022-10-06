import random

carta1jugador=int(random.uniform(1,13))


sumatoriajugador=int

#JUEGO DEL USUARIO
print("Tu carta es " + str(carta1jugador))
print("\nQuieres otra carta?")
# Se despliega el menu
print("1. Si.")
print("2. No.")
decision1jugador=int(input("Digita tu eleccion: "))


if decision1jugador==1:
    carta2jugador=int(random.uniform(1,13))
    print("\nTu carta es " + str(carta2jugador))
    sumatoriajugador= carta1jugador + carta2jugador

    if sumatoriajugador < 22:
        print("\nQuieres otra carta?")
        # Se despliega el menu
        print("1. Si.")
        print("2. No.")
        decision2jugador=int(input("Digita tu eleccion: "))
    
    
        if decision2jugador==1:
            carta3jugador=int(random.uniform(1,13))
            print("\nTu carta es " + str(carta3jugador))
            sumatoriajugador=carta1jugador + carta2jugador + carta3jugador

            if sumatoriajugador<22:
                print("\nQuieres otra carta?")
                # Se despliega el menu
                print("1. Si.")
                print("2. No.")
                decision3jugador=int(input("Digita tu eleccion: "))

                if decision3jugador==1:
                    carta4jugador=int(random.uniform(1,13))
                    print("\nTu carta es " + str(carta3jugador))
                    sumatoriajugador=carta1jugador + carta2jugador + carta3jugador + carta4jugador

                    if sumatoriajugador<22:
                        print("\nQuieres otra carta?")
                        # Se despliega el menu
                        print("1. Si.")
                        print("2. No.")
                        decision4jugador=int(input("Digita tu eleccion: "))

                        if decision4jugador==1:
                            carta5jugador=int(random.uniform(1,13))
                            print("\nTu carta es " + str(carta5jugador))
                            sumatoriajugador= carta1jugador + carta2jugador + carta3jugador + carta4jugador + carta5jugador

                            if sumatoriajugador<22:
                                print("\nTus puntos son: " ,sumatoriajugador)
                            
                            else:
                                print("PERDISTE")


                        if decision4jugador==2:
                            sumatoriajugador=carta1jugador + carta2jugador + carta3jugador + carta4jugador
                            print("\nTus puntos son: " ,sumatoriajugador)
                    else:
                        print("PERDISTE")
                    
                if decision3jugador==2:
                    sumatoriajugador=carta1jugador + carta2jugador + carta3jugador
                    print("\nTus puntos son: " ,sumatoriajugador)

            else:
                print("PERDISTE")
            
        if decision2jugador==2:
            sumatoriajugador=carta1jugador + carta2jugador
            print("\nTus puntos son: " ,sumatoriajugador)
    else:
        print("PERDISTE")
    
if decision1jugador==2:
    sumatoriajugador=carta1jugador
    print("\nTus puntos son: " ,sumatoriajugador)          


#JUEGO COMPUTADOR
if sumatoriajugador<=21:
    sumatoriacomputador=0

    while sumatoriacomputador<sumatoriajugador:
        cartacomputador=int(random.uniform(1,13))
        sumatoriacomputador = sumatoriacomputador + cartacomputador

    print("\nLos puntos del computador son: " + str(sumatoriacomputador))
    if sumatoriacomputador>21:
        print("\nGANASTE!!")
    else:
        print("\nPERDISTE!!")


