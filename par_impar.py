# Programa para saber que numero es par o impar

#input
x = int(input("digite un numero "))

#processing
r=x%2
if r==0:
    msj="PAR"
else:
    msj="IMPAR"

print("El numero " + str(r) + "es" + msj)
    