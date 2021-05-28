################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_centigrados(fahrenheit):
    centigrados= ((float (fahrenheit)-32)/1.8)
    return centigrados

def prueba():
    fahrenheit=input ("ingrese grados fahrenheit")
    print (f"el resultados es {convertir_a_centigrados(fahrenheit)}")

if __name__ == "__main__":
    prueba()
    