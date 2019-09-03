def ordenada(lista):
    listaAComparar = []
    respuesta = False
    for i in lista:
        listaAComparar.append(i)
    else:
        lista.sort()
    
    if lista == listaAComparar:
        respuesta = True

    print(respuesta)
    
        

ordenada([1, 2, 3, 4, 5, 6])


