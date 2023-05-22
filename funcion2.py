# Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro
# , un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del
#  segundo parámetro por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la
#  cadena

def reemplazarCaracteres(cadena:str,caracter_uno:str,caracter_dos:str)->str:
    """reemplaza caracteres recibidos de una cadena, buscando el primer parametro para reemplazarlo por el segundo

    Args:
        cadena (str): texto a evaluar
        caracter_uno (str): parametro a buscar
        caracter_dos (str): parametro a cambiar

    Returns:
        str: retorna la cadena con los cambios
    """
    aux = ""
    for letra in cadena:
        if letra == caracter_uno:
            aux += caracter_dos
        else:
            aux += letra
    return aux

print(reemplazarCaracteres("pepito","t","z"))