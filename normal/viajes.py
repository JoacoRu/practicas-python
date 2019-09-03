def porcentaje(n, porcentaje):
    """ Calcula el porcentaje ingresando un numero y la cantidad de porcentaje. Retorna el porcentaje de esa cantidad """
    multi = porcentaje * n
    return multi / 100

def subte(viajes, tarifa):
    """ Devuelve el total gastado segun la tarifa decreciente del subte """
    historialDeGastos = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0
    }
    total = viajes * tarifa
    if viajes < 21:
        historialDeGastos['0'] = total
    elif viajes >= 21 and viajes <= 30:
        viajes -= 20
        historialDeGastos['0'] = 20 * tarifa
        historialDeGastos['1'] = porcentaje(viajes, tarifa)
    elif viajes >= 31 and viajes <= 40:
        viajes -= 30
        historialDeGastos['0'] = 20 * tarifa
        historialDeGastos['1'] = porcentaje(10, tarifa)
        historialDeGastos['2'] = porcentaje(viajes, tarifa)
    elif viajes >= 40:
        viajes -= 40
        historialDeGastos['0'] = 20 * tarifa
        historialDeGastos['1'] = porcentaje(10, tarifa)
        historialDeGastos['2'] = porcentaje(10, tarifa)
        historialDeGastos['2'] = porcentaje(viajes, tarifa)

    print(historialDeGastos['0'] + historialDeGastos['1'] + historialDeGastos['2'] + historialDeGastos['3'])
        

subte(22, 30)