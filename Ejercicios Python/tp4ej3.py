################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrenheit(centigrados):
    fahrenheit= ((float(centigrados)*1.8)+32)
    return fahrenheit
def prueba():
    centigrados= input("ingrese grados centigrados")
    print (f"el resultados es {convertir_a_fahrenheit(centigrados)}")

if __name__ == "__main__":
    prueba()
