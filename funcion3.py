# Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y
#  su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenar_caracteres(cadena:str)->str:
    """ordenar los caracteres de manera ascendente dentro de la cadena.

    Args:
        cadena (str): Cadena que debe ordenarze ascendentemente

    Returns:
        str: cadena ordenada
    """
    aux_cadena = list(cadena)
    retorno = ""

    for i in range(len(aux_cadena)):
        for j in range(i+1, len(aux_cadena)):
            if aux_cadena[i] > aux_cadena[j]:
                aux = aux_cadena[j]
                aux_cadena[j] = aux_cadena[i]
                aux_cadena[i] = aux

    for letra in aux_cadena:
        retorno += letra

    return retorno

def ordenar_numeros(cadena:list)->list:

    for i in range(len(cadena)):
        for j in range(i+1, len(cadena)):
            if cadena[i] > cadena[j]:
                aux = cadena[j]
                cadena[j] = cadena[i]
                cadena[i] = aux

    return cadena

print(ordenar_caracteres("algoritmo"))
print(ordenar_numeros([0,8,45,1,320,21,51,10,2]))