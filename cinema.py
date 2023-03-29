def calcular_precio(sala, num_boletas, hora_pico, pago_tarjeta_cinema, reserva):
    
    sala_3d = 15500
    sala_2d = 11300
    sala_dinamix = 18800
    
    descuento_hora_no_pico = 0.1
    descuento_mas_de_tres_boletas = 500
    descuento_pago_tarjeta = 0.05
    recargo_reserva = 2000
    
    
    incremento_sala_2d_3d = 0.25
    incremento_sala_dinamix = 0.5
    
    if sala == "3d":
        precio_base = sala_3d
    elif sala == "2d":
        precio_base = sala_2d
    elif sala == "dinamix":
        precio_base = sala_dinamix
    else:
        return "Tipo de sala no válido"
    
    if hora_pico:
        if sala == "3d" or sala == "2d":
            precio_base *= (1 + incremento_sala_2d_3d)
        elif sala == "dinamix":
            precio_base *= (1 + incremento_sala_dinamix)
    
    
    if not hora_pico:
        precio_base *= (1 - descuento_hora_no_pico)
    
    if num_boletas >= 3:
        descuento_por_boleta = descuento_mas_de_tres_boletas / num_boletas
        precio_base -= descuento_por_boleta
    
    
    if pago_tarjeta_cinema:
        precio_base *= (1 - descuento_pago_tarjeta)
    
    
    if reserva:
        precio_base += recargo_reserva
    
    return precio_base * num_boletas

    return precio_total

sala = input("Ingrese el tipo de sala (3d, 2d, dinamix): ")
num_boletas = int(input("Ingrese el número de boletas: "))
hora_pico = input("¿Es hora pico? (si/no): ").lower() == "si"
pago_tarjeta_cinema = input("¿Va a pagar con tarjeta de cinema? (si/no): ").lower() == "si"
reserva = input("¿Va a hacer una reserva? (si/no): ").lower() == "si"
precio_total = calcular_precio(sala, num_boletas, hora_pico, pago_tarjeta_cinema, reserva) 
print("El precio total es:", precio_total)




