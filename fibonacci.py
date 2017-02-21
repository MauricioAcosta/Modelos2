print ('Serie de fibonacci')
num=int(input('Ingrese un numero entero\n'))

def fibonacci(num):
    if (num==0 or num==1):
        return num
    else:
        return fibonacci(num-2)+fibonacci(num-1)

for x in range (0,num):
   print( fibonacci(x))
