def mayor(num, num_d, num_t):
    respuesta = ''
    
    if num > num_d:
        if num > num_t:
            respuesta = num
        else: 
            if num_t > num_d:
                respuesta = num_t
    elif num_d > num_t:
        if num_d > num:
            respuesta = num_d
    else:
        respuesta = num_t
    
    print(respuesta)

mayor(3000, 1500, 1800)