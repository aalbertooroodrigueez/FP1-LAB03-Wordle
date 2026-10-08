from datetime import datetime

def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    return len(cadena) == 5 and cadena.isalpha()


def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    diferencia = fin - inicio
    total_segundos = int(diferencia.total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return (minutos, segundos)


def quitar_letra(cadena: str, letra: str) -> str:
    posicion = cadena.find(letra)
    if posicion != -1:
        return cadena[:posicion] + cadena[posicion + 1:]
    return cadena


def marcar_verdes(palabra_secreta: str, intento: str) -> tuple:
    verdes = ""
    restantes = palabra_secreta

    for i in range(5):
        if palabra_secreta[i] == intento[i]:
            verdes += "V"
            restantes = quitar_letra(restantes, intento[i])
        else:
            verdes += "_"

    return (verdes, restantes)


def marcar_amarillos(intento: str, verdes: str, restantes: str) -> str:
    colores = ""

    for i in range(5):
        if verdes[i] == "V":
            colores += "V"
        else:
            letra_intento = intento[i]
            if letra_intento in restantes:
                colores += "A"
                restantes = quitar_letra(restantes, letra_intento)
            else:
                colores += "_"

    return (colores)

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    verdes, restantes = marcar_verdes(palabra_secreta, intento)
    return marcar_amarillos(intento, verdes, restantes)