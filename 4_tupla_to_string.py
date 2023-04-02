def imprimir_tupla():
    # Solicitar al usuario los valores de la tupla
    valores = input("Introduce los valores de la tupla separados por comas: ")
    
    # Convertir los valores en una tupla
    tupla = tuple(valores.split(","))
    
    # Imprimir la tupla
    print(tupla)
