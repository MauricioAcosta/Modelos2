# -*- coding: cp1252 -*-
print ("Binario a Decimal y Decimal a Binario")
print ("Menu")
print ("Decimal a Binario ingrese: a")
print ("Binario a Decimal ingrese: b")
opcion = input("¿Que quieres hacer?")

if opcion == "a" :
    print ("Introduce el numero decimal y se convertira en un numero binario")
    ndcimal = int(input("Introduce el numero: "))
    print ("El numero en Binario es: %s " % bin(ndcimal))



if opcion == "b" :
    print ("Introduce el numero binario y se convertira en un numero decimal")
    print("Nota: inicializa el binario con: 0b")
    nbinario = str(input("Introduce el numero : "))
    print ("El numero en Decimal es: %s " % int(nbinario,2))
