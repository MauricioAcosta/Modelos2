print ('Potencia de n a la m')
num=int(input('Ingrese el Numero a elevar \n'))
num2=int(input('Ingrese el Numero de la potencia \n'))
def potencia(num,num2):
    if num2==0:
        return 1
       
    else:
        return num*(potencia(num,num2-1))
print (potencia(num,num2))
