print ('Suma de dos numeros')
num=int(input('Ingrese un numero 1\n'))
num2=int(input('Ingrese un numero 2\n'))
def Suma(num,num2):
    if (num==0):
        return num2
    else:
        if(num2!=0):
            return Suma(num,num2-1)+1
        else:
            return Suma(num-1,num2)+1
print( Suma(num,num2))
