#!/bin/python3
class Nodo_nario:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
    def __str__(self):
        return str(self.valor)
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

def menor(lista):
    if len(lista) == 1:
        return lista[0]
    for i in lista:
        if(i < lista[len(lista)-1]):
            return menor(lista[0:len(lista)-1])
        else:
            return menor(lista[1:])

def ordenar(lista):
    if lista == []:
        return []
    else:
        return [menor(lista)] + ordenar([x for x in lista if(x != menor(lista))])

def arbolPadre(lista, arbol):
    if arbol == None:
        return arbolPadre(lista[1:], Nodo_nario(lista[0]))
    elif lista == []:
        return arbol
    else:
        verticeAnterior(arbol, lista[0]).agregarHijo(Nodo_nario(lista[0]))
        return arbolPadre(lista[1:], arbol)
def subArbol(arbol, valor):
    if arbol.valor == valor:
        return arbol
    for sub in arbol.hijos:
        if (subArbol(sub, valor) != None):
            return subArbol(sub, valor)
    return None
def verticeAnterior(arbol, vertice):
    if len(vertice) == 1:
        return arbol
    else:
        if(subArbol(arbol, vertice) != None):
            return subArbol(arbol, vertice)
        else:
            return verticeAnterior(arbol, vertice[0:(len(vertice)-1)])
def arbolCreado(arbol):
    print (arbol.valor)
    for hijo in arbol.hijos:
        arbolCreado(hijo)

print(ordenar(['a','ab','ac','abel','abeto','abatia','acacia']))
myTree = arbolPadre(ordenar(['a','ab','ac','abel','abeto','abatia','acacia']),None)
arbolCreado(arbolPadre(ordenar(['a','ab','ac','abel','abeto','abatia','acacia']),None))
