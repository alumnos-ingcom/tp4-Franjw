################
# Francsico Jwanczyk - @franjw
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def ordenar_mayor_a_menor(uno, dos, tres):
    if (uno > dos) and (uno > tres):
        print(uno)
        if (dos>tres):
            print (dos)
            print (tres)
        elif (tres>dos):
            print(tres)
            print(dos)
    elif (uno<dos) and (dos>tres):
        print(dos)
        if (tres>uno):
            print(tres)
            print(uno)
        elif(uno>tres):
            print(uno)
            print(tres)
    elif (tres>dos)and(tres>uno):
        print(tres)
        if(dos>uno):
            print(dos)
            print(uno)
        elif (dos<uno):
            print(uno)
            print(dos)

def ordenar_menor_a_mayor(uno, dos, tres):
    if (uno < dos) and (uno < tres):
        print(uno)
        if (dos<tres):
            print (dos)
            print (tres)
        elif (tres<dos):
            print(tres)
            print(dos)
    elif (uno>dos) and (dos<tres):
        print(dos)
        if (tres<uno):
            print(tres)
            print(uno)
        elif(uno<tres):
            print(uno)
            print(tres)
    elif (tres<dos)and(tres<uno):
        print(tres)
        if(dos<uno):
            print(dos)
            print(uno)
        elif (dos>uno):
            print(uno)
            print(dos)
    
        
    
                        
def prueba():
    uno =int(input("ingrese un numero"))
    dos =int(input("ingrese un numero"))
    tres =int(input("ingrese un numero"))
    print("ordenado de mayor a menor",ordenar_mayor_a_menor(uno, dos, tres))
    print("ordenado de menor a mayor",ordenar_menor_a_mayor(uno, dos, tres))

if __name__ == "__main__":
    prueba()
        
    
        
    
        