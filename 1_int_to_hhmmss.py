def convert_seconds_to_hms(seconds):
    # Calculamos las horas, minutos y segundos
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    # Mostramos el resultado en pantalla
    print("Horas: {}, Minutos: {}, Segundos: {}".format(hours, minutes, seconds))

# Pedimos al usuario que ingrese el número de segundos
while True:
    try:
        seconds = int(input("Ingresa el número de segundos: "))
        if seconds < 0:
            raise ValueError("Debe ingresar un número entero positivo.")
        break
    except ValueError:
        print("Debe ingresar un número entero positivo.")

# Convertimos los segundos a horas, minutos y segundos e imprimimos el resultado
convert_seconds_to_hms(seconds)
