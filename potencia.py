def potencia(n,m):
	valor=pow(n,m)
	return valor

num=int(input("Ingrese el numero: "))
pot=int(input("Ingrese la potencia: "))
valor=potencia(num,pot)
print("La potencia de ",num," eleveado a la ", pot, " es: ",valor )
