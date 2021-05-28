################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def division_lenta(dividendo, divisor):
    cociente=0
    while dividendo >= divisor:
        dividendo= dividendo-divisor
        cociente +=1
        print("el cociente es", cociente)
        print("el resto es", dividendo)

def prueba():
    dividendo= int(input("ingrese el dividendo"))
    divisor=int(input("ingrese un divisor"))
    print(division_lenta(dividendo, divisor))

if __name__ == "__main__":
    prueba()