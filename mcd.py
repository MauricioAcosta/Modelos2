def mcd(numero1,numero2):
	if numero2 == 0:
		return numero1
	return mcd(numero2, numero1 % numero2)
 

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
 
print("El máximo común divisor de ", numero1," y ", numero2," es ", mcd(numero1, numero2))

