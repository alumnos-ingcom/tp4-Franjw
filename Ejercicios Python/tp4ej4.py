################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, numero2):
    if numero == numero2:
        return 0
    elif numero < numero2:
        return -1
    elif numero > numero2:
        return 1

def prueba():
    numero= input("ingrese un numero")
    numero2=input("ingrese otro numero")
    print (compara(numero, numero2))

if __name__ == "__main__":
    prueba()
