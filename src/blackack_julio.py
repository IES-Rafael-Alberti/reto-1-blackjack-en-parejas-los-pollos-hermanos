def crear_baraja():
    return "A234567890JQK"


def sumar_puntuacion(mano):
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


