import random
def generadorDeLista():
    lista = []

    for i in range(0, 10):
        lista.append(random.randint(1, 50))

    return lista

def obtenerUltimoIndice(lista):

    return len(lista) - 1

def interseccion():
    lista_uno = generadorDeLista()
    lista_dos = generadorDeLista()
    lista_tres = []

    ultimo_indice = lista_uno[obtenerUltimoIndice(lista_uno)]
    primer_indice = lista_dos[0]

    if ultimo_indice > primer_indice:
        ultimo_indice = lista_dos[obtenerUltimoIndice(lista_dos)]
        primer_indice = lista_uno[0]
        for i in range(ultimo_indice + 1, primer_indice):
            lista_tres.append(i)
        else:
            print(lista_dos, lista_tres, lista_uno, 'lista_uno')

    else:
        for i in range(ultimo_indice + 1, primer_indice):
            lista_tres.append(i)
        else:
            print(lista_uno, lista_tres, lista_dos, 'lista_dos')



interseccion()