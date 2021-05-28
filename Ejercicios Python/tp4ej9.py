################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factores_primos(numero):
    if numero==1:
        return False
    elif numero==2:
        return True
    else:
        for i in range(2,numero):
            if numero % i==0:
                return False
        return True
            

def prueba():
    numero=int(input("ingrese un numero para ver si es primo"))
    print(factores_primos(numero))

if __name__ == "__main__":
    prueba()   



            
        
        