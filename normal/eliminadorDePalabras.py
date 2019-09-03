def eliminadorDeListas(nombres, nombresEliminar):
    """Elimina los nombres de una lista dados en el arg nombresEliminar"""
    for i in nombres:
        if i in nombresEliminar:
            nombres.remove(i)
    
    print(nombres)
    print(nombresEliminar)

lista = ['koalita', 'no', 'es', 'toxica']
listaDos = ['no']

eliminadorDeListas(lista, listaDos)