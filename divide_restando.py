print ('Divide restando')
num=int(input('Ingrese el dividendo\n'))
num2=int(input('Ingrese el divisor \n'))
def dividir(num,num2):
    if num<num2:
        return 0
       
    else:
        return dividir(num-num2,num2)+1
print (dividir(num,num2))
