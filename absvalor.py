def valor(numero):
	if numero>=0:
		return numero
	else:
		return valor(-numero)

num=int(input("Ingresa un numero: "))
print("El valor absoluto de", num," es: ",valor(num))
