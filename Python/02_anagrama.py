"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(palabra1, palabra2):
    palabra1 = set(palabra1) 
    palabra2 = set(palabra2)

    if palabra1 == palabra2:
        return True
    else:
        return False
    
respuesta = anagrama("amor", "roma")
print(respuesta)
