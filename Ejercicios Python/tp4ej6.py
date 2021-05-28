################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    menor=lista[0]
    
    for n in lista:
        if n < menor:
            menor=n
            return menor
def maximo(lista):
    mayor=lista[0]
    
    for n in lista:
        if n > mayor:
            mayor=n
            return mayor

def prueba():
    valor1= int(input ("ingrese un numero"))
    valor2= int(input ("ingrese un numero"))
    valor3= int(input ("ingrese un numero"))
    lista= [valor1, valor2, valor3]
    print (f"el numero menor es{minimo(lista)}")
    print (f"el numero mayor es{maximo(lista)}")

if __name__ == "__main__":
    prueba()   