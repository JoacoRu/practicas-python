import random

def generateList():
    lista = []
    numero = 0
    contador = 0
    for i in range(50):
        lista.append(random.randint(1, 100))
    return lista

def elementoRepetido(lista):
    unicos = []
    repetidos = []

    for i in lista:
        if i not in unicos:
            unicos.append(i)
        else:
            repetidos.append(i)
    else:
        if(len(repetidos) > 0):
            return True
        else:
            return False

def devolverUnicos(lista):
    unicos = []

    for i in lista:
        if i not in unicos:
            unicos.append(i)
        else:
            lista.remove(i)
    else:
        print(lista)

devolverUnicos(generateList())