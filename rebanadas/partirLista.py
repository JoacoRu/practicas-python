import random

def generador_de_lista():
    lista = []
    for i in range(0, random.randint(10, 50)):
        lista.append(random.randint(0, 100))
    else:
        return lista


def partir_lista(lista):
    longitud_divisoria = int((len(lista) - 1)  / 2)
    primera_mitad = lista[longitud_divisoria: ]
    segunda_mitad = lista[ :-longitud_divisoria -1]
    lista_dos = []
    lista_tres = []
    
    print(lista, segunda_mitad, primera_mitad)


partir_lista(generador_de_lista())
    


