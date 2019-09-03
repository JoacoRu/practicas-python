import random

def generadorDeLista():
    """ Genera una lista con numero al azar entre 1 y 200 """
    lista = []
    
    for i in range(random.randint(1, 5)):
        lista.append(random.randint(1, 200))
    
    return lista

def sumadorDeLista():
    lista = generadorDeLista()
    nuevaLista = []
    for i in lista:
        indice = lista.index(i) 
        if(indice == 0):
            nuevaLista.append(i)
        elif(indice == 1):
            nuevaLista.append(lista[indice - 1] + i)
        else:
            nuevaLista.append(nuevaLista[indice -1] + i)

    return nuevaLista

sumadorDeLista()