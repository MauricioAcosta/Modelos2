#!/usr/bin/python3

def contar_mano(lista_cartas):
    """retorna el valor de la mano"""
    if lista_cartas == []:
        return 0
    if type(lista_cartas[0][0]) == str:
        if lista_cartas[0][0] == 'A':
            return 1 + contar_mano(lista_cartas[1:])
        else:
            return 10 + contar_mano(lista_cartas[1:])
    else:
        return lista_cartas[0][0] + contar_mano(lista_cartas[1:])

def ajustar_resultado(lista_cartas, mano):
    """cuentas las 'A' y suma 10 de ser posible"""
    if lista_cartas == []:
        return mano

    if mano < 12:
        if lista_cartas[0][0] == "A":
            return ajustar_resultado(lista_cartas[1:], mano+10)
        else:
            return ajustar_resultado(lista_cartas[1:], mano)
    return mano

cartas = [[4,"C"],["A","P"],["A","D"],[3,"C"],[2,"P"]]
mano = contar_mano(cartas)
res = ajustar_resultado(cartas, mano)

print("Primer conteo :{}\nConteo teniendo en cuenta las 'A': {}".format(mano,res))
