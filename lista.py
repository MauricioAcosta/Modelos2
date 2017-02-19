def reversa (lista):
            if len(lista)==0:
                return lista
            else:
                return [lista[-1]]+reversa(lista[0:-1])
lista=[]
for i in range(0,10):
    lista.append(input("Ingresa los datos: "))
print(reversa(lista))
