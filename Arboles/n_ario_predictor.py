class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

def agregarElemento(elementoPadre, elemento):
    elemento = Arbol(elemento)
    elementoPadre.hijos.append(elemento)
    return elemento

arbolP0 = Arbol('p')
arbolE1 = agregarElemento(arbolP0,'e')
arbolD2 = agregarElemento(arbolE1,'d')
arbolA3 = agregarElemento(arbolD2,'a')
arbolR30 = agregarElemento(arbolD2,'r')
arbolO40 = agregarElemento(arbolR30,'o')
arbolR2 = agregarElemento(arbolE1,'r')
arbolO3 = agregarElemento(arbolR2,'o')
arbolR31 = agregarElemento(arbolR2,'r')
arbolA4 = agregarElemento(arbolR31,'a')
arbolO41 = agregarElemento(arbolR31,'o')
arbolZ2 = agregarElemento(arbolE1,'z')

def buscar1(nivel, indice, letras, hijos, palabra):
    #print(nivel, len(hijos), indice)
    #print(nivel >= len(letras), indice < len(hijos))
    while indice < len(hijos):
        if nivel >= len(letras): # no existe letras[nivel]
            palabra.append(hijos[0].elemento)
            return buscar1(nivel + 1, 0, letras, hijos[0].hijos, palabra)
        elif letras[nivel] == hijos[indice].elemento:
            #print(letras[nivel])
            palabra.append(hijos[indice].elemento)
            return buscar1(nivel + 1, 0, letras, hijos[indice].hijos, palabra)
        else:
            indice += 1
    return palabra

buscar1(0, 0, ["p", "e", "d", "r"], [arbolP0], [])
