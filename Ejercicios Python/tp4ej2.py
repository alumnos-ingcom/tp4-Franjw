################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero1, numero2):
   resultado= numero1 + numero2
   
   print ("el resultado es")   
   while numero1 < resultado:
       numero1 +=1
       print (numero1)
   
   while numero1 > resultado:
       numero1 -=1
       print (numero1)
   
       
def prueba ():
    numero1= int(input("ingrese un numero"))
    numero2= int(input("ingrese otro numero"))
    suma_lenta(numero1, numero2)
    
if __name__ == "__main__":
    prueba()
