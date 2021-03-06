class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def inorden(arbol):
	if arbol==None:
		return ""
	else:
		return inorden(arbol.izquierda)+arbol.valor+inorden(arbol.derecha)

def buscar(arbol,valor):
	if arbol==None:
		return False
	elif arbol.valor==valor:
		return True
	else:
		return buscar(arbol.izquierda) or buscar(arbol.derecha)

def evaluar(arbol):
	if arbol.valor=='+':
		return evaluar(arbol.izquierda)+evaluar(arbol.derecha)
	elif arbol.valor=='-':
		return evaluar(arbol.izquierda)-evaluar(arbol.derecha)
	elif arbol.valor=='*':
		return evaluar(arbol.izquierda)*evaluar(arbol.derecha)
	elif arbol.valor=='/':
		return evaluar(arbol.izquierda)/evaluar(arbol.derecha)
	else:
		return int(arbol.valor)


print (evaluar(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))
