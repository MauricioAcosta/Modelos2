def binario_a_decimal(binario,orden):
    d=0
    operacion=0
    if binario<10:
        operacion=(binario%2)*(2**orden)
        d=d+operacion
        return d
    else:
        binario_a_decimal(binario//10,orden-1)
        operacion=(binario%2)*(2**orden)
        d=d+operacion
        return d
print("ingrese el numero binario")
numero=input()
binario_a_decimal(int(numero),len(numero))
print(d)

