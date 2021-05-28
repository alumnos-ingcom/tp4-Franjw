################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    if numero == 0:
        return"es 0"
    
    elif numero > 0:
        return"es positivo"

    elif numero < 0:
        return"es negativo"

def prueba():
    numero= int(input("ingrese un numero"))
    print (signo(numero))

if __name__ == "__main__":
    prueba()