def listaCuadrada():
    n = int(input("Porfavor ingrese un valor numerico"))
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    
    return lista

def ultimosDiez(lista):
    hasta = len(lista)
    desde = hasta - 10
    otraLista = []
    for i in range(desde, hasta):
        otraLista.append(lista[i])

    print(otraLista, lista)
        

ultimosDiez(listaCuadrada())