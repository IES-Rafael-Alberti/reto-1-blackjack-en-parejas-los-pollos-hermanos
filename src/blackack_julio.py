import random


def crear_baraja() -> str:
    return "A234567890JQK"


def plantarse() -> bool:
    plantado = None

    while plantado is None:
        try:
            comando = input("Deseas plantarte? (s/n): ")
            comando = comando.upper()
            if comando == "S":
                plantado = True
            elif comando == "N":
                plantado = False
            else:
                raise ValueError(comando, "Es una opcion no valida")
        except ValueError:
            print("Has introducido un dato invalido")

    return plantado


def sumar_puntuacion(mano: str) -> int:
    puntuacion = 0
    ases = 0

    for carta in mano:
        match carta:
            case "A":
                ases += 1
            case "2":
                puntuacion += 2
            case "3":
                puntuacion += 3
            case "4":
                puntuacion += 4
            case "5":
                puntuacion += 5
            case "6":
                puntuacion += 6
            case "7":
                puntuacion += 7
            case "8":
                puntuacion += 8
            case "9":
                puntuacion += 9
            case _:
                puntuacion += 10

    puntuacion += ases * 10
    for i in range(0, ases):
        if puntuacion > 21:
            puntuacion -= 9
    return puntuacion


def info_jugador(nombre: str, mano: str, puntuacion: int) -> str:
    if puntuacion > 21:
        puntuacion = "**se pasa**"
    else:
        puntuacion = "(" + str(puntuacion) + ")"
    return " - {} - {} {}".format(nombre, mano, str(puntuacion))


def resultado_final(nombre1: str, punt_j1: int, nombre2: str, punt_j2: int) -> str:
    if punt_j1 > 21 and punt_j2 > 21:
        return "Game over ¡Los dos os habeis pasado!"
    elif punt_j1 <= 21 and punt_j1 == punt_j2:
        return "¡Empate!"
    elif (punt_j2 < punt_j1 <= 21) or (punt_j1 <= 21 < punt_j2):
        return "¡Gana J1 - " + nombre1
    else:
        return "¡Gana J2 - " + nombre2


def dar_carta(baraja: str, mano: str) -> str:
    mano += baraja[random.randint(0, len(baraja) - 1)]
    return mano
