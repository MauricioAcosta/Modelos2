#!/usr/bin/env python3
class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

class Predictor:
    def __init__(self):
        arbolP0 = Arbol('p')
        arbolE1 = self.agregarElemento(arbolP0,'e')
        arbolD2 = self.agregarElemento(arbolE1,'d')
        arbolA3 = self.agregarElemento(arbolD2,'a')
        arbolR30 = self.agregarElemento(arbolD2,'r')
        arbolO40 = self.agregarElemento(arbolR30,'o')
        arbolR2 = self.agregarElemento(arbolE1,'r')
        arbolO3 = self.agregarElemento(arbolR2,'o')
        arbolR31 = self.agregarElemento(arbolR2,'r')
        arbolA4 = self.agregarElemento(arbolR31,'a')
        arbolO41 = self.agregarElemento(arbolR31,'o')
        arbolZ2 = self.agregarElemento(arbolE1,'z')
        self.arbol = arbolP0

    def agregarElemento(self, elementoPadre, elemento):
        elemento = Arbol(elemento)
        elementoPadre.hijos.append(elemento)
        return elemento

    def buscarPorPalabra(self, palabras):
        listaPalabras = list(palabras)
        def buscarPorLista(nivel, indice, letras, hijos, palabra):
            #print(nivel, len(hijos), indice)
            #print(nivel >= len(letras), indice < len(hijos))
            while indice < len(hijos):
                if nivel >= len(letras): # no existe letras[nivel]
                    palabra.append(hijos[0].elemento)
                    return buscarPorLista(nivel + 1, 0, letras, hijos[0].hijos, palabra)
                elif letras[nivel] == hijos[indice].elemento:
                    #print(letras[nivel])
                    palabra.append(hijos[indice].elemento)
                    return buscarPorLista(nivel + 1, 0, letras, hijos[indice].hijos, palabra)
                else:
                    indice += 1
            return palabra

        return "".join(buscarPorLista(0, 0, listaPalabras, [self.arbol], []))
