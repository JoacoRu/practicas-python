def esFecha(dia, mes, ano):
    fecha = []
    respuesta = False
    if dia <= 31 and dia > 0:
        fecha.insert(0, True)
    else:
        fecha.insert(0, False)
    
    if mes <= 12 and mes >= 0:
        fecha.insert(1, True)        
    else:
        fecha.insert(1, False)

    if ano > 0 and ano < 2019:
        fecha.insert(2, True)
    else: 
        fecha.insert(2, False)        

    if fecha[0] and fecha[1] and fecha[2]:
        respuesta = True
    
    print(respuesta)

esFecha(32, 2, 1998)

    