def factorial(valor,numero):
	if(numero>0):
		valor=factorial(valor,numero-1)
		valor=valor*numero
	else:
		valor=1
	return valor
num=int(input("Inserte un numero: "))

calculo=factorial(1,num)

print ("El factorial de ",num," es: ",calculo)
