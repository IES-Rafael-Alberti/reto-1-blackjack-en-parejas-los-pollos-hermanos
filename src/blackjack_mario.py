
# Se actualiza la baraja en caso de que se agoten las cartas (MAXIMO 4 DE CADA)
def actualizar_baraja(baraja, manos): 
    for carta in manos:
        repetido_cadena = manos.count(carta)
        if repetido_cadena == 4:
            baraja=baraja.replace(carta, "")
    return baraja

# Suma de las manos de los jugadores
def suma_mano(mano1, mano2):
    manos_total=mano1+mano2
    return manos_total

def main():
    baraja = "A234567890JQK"  # Lista de cartas a contar
    mano1 = "AA20" # Mano de cartas del jugador1
    mano2 = "AA20" # Mano de cartas del jugador2
    
    actualizar_baraja(baraja, suma_mano(mano1, mano2))

if __name__ == "__main__":
    main()