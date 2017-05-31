def tabla (valor,multi):
	if multi>0 and (valor>0 or valor<0):
		if multi==1:
			return valor
		else:
			return valor+(tabla(valor,multi-1))
	else:
		return 0
valor=int(input("Ingrese el numero: "))
multi=int(input("Por cuanto lo desea multiplicar: "))
resultado=tabla(valor,multi)
print("el numero ",valor," * ", multi," es: ",resultado)
