class tree():
    def __init__(self , valor  , izquierda=None , derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def entrada(preg):
    print (preg)
    return input('Respuesta : \t 1) Si \t 2) No\n')

def busqueda_rec(arbol):
    if arbol.izquierda==None:
        return arbol.valor
    else:
        if entrada(arbol.valor)=='1':
            return busqueda_rec(arbol.izquierda)
        else:
            return busqueda_rec(arbol.derecha)

arbol=tree(["a",tree("ab",tree("abel"),tree("abeto"),tree("abatia")),tree("ac"),tree("acacia")])

print (busqueda_rec(arbol))
