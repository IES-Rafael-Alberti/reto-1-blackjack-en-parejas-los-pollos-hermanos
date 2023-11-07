# Indicar modo de juego y nombres de los jugadores
def inicio_juego():
    modo=input("Indica el modo de juego [SINGLEPLAYER//MULTIPLAYER]: ")
    modo=modo.upper()
    if modo=="SINGLEPLAYER":
        nombre_j1=input("Jugador 1, introduce tu nombre: ")
        nombre_maquina="PC_de_Pepito"
        return nombre_j1, nombre_maquina
    elif modo=="MULTIPLAYER":
        nombre_j1=input("Jugador 1, introduce tu nombre: ")
        nombre_j2=input("Jugador 2, introduce tu nombre: ")
        return nombre_j1, nombre_j2

# Estado del jugador (PERDER/CONTINUAR JUGANDO/PLANTARSE)
def estado_jugador(puntuacion, plantado):
    if puntuacion > 21:
        return #LOSE
    elif puntuacion < 21 and puntuacion >= 0:
        return #CONTINUE 
    elif plantado==True:
        return #PLANTADO (A LA ESPERA DEL OTRO J2)

# Se actualiza la baraja en caso de que se agoten las cartas (MAXIMO 4 DE CADA)
def actualizar_baraja(baraja, manos): 
    for carta in manos:
        repetido_cadena = manos.count(carta)
        if repetido_cadena == 4:
            baraja=baraja.replace(carta, "")
    return baraja

# Suma de las manos de los jugadores
def suma_mano(mano1, mano2):
    manos_total = mano1 + mano2
    return manos_total

def main():
    baraja = "A234567890JQK"  # Lista de cartas a contar
    mano1 = "AA20" # Mano de cartas del jugador1
    mano2 = "AA20" # Mano de cartas del jugador2
    
    actualizar_baraja(baraja, suma_mano(mano1, mano2))

if __name__ == "__main__":
    main()