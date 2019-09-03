import random

def generadorDeLista():
    """ Genera una lista con numero al azar entre 1 y 200 """
    lista = []
    
    for i in range(random.randint(1, 5)):
        lista.append(random.randint(1, 200))
    
    return lista

def superPosicion(lista_uno, lista_dos):
    """ Dice si una lista contine los elementos de la otra lista """
    contiene = False
    for i in lista_uno:
        if(i in lista_dos):
            contiene = True
    else:
        print(contiene)
        print(lista_uno)
        print(lista_dos)

superPosicion(generadorDeLista(), generadorDeLista())