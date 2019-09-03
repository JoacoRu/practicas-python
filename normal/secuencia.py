def esMayor(n):
    respuesta = True
    if(not 100 >= n):
        respuesta = False
    return respuesta

def secuencia(n):
    suma = []
    if not esMayor(n):
        print('El numero no es valido')
    else:
        for i in range(1, n, 4):
            suma.append(i**2)
        else:
            print(suma, 'Resultados de potenciacion')
            print(sum(suma), 'Resultado total')

secuencia(30)