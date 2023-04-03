# Función para añadir una nueva factura al diccionario
def agregar_factura(facturas):
    numero_factura = input("Escriba el número de factura (de 4 dígitos): ")
    costo_factura = float(input("Escriba el costo de la factura: "))
    facturas[numero_factura] = costo_factura
    print("Factura añadida correctamente:")
    print(facturas)

# Función para pagar una factura existente en el diccionario
def pagar_factura(facturas):
    numero_factura = input("Escriba el número de factura que desea pagar: ")
    if numero_factura in facturas:
        costo_factura = facturas[numero_factura]
        del facturas[numero_factura]
        print(f"Se ha pagado la factura número {numero_factura} por un costo de {costo_factura}")
    else:
        print(f"La factura número {numero_factura} no existe")

# Función para imprimir la cantidad cobrada hasta el momento y la cantidad pendiente de cobro
def imprimir_cantidades(facturas):
    cantidad_cobrada = sum(facturas.values())
    cantidad_pendiente = 0
    if cantidad_cobrada > 0:
        cantidad_pendiente = sum(facturas.values()) - cantidad_cobrada
    print(f"Cantidad cobrada hasta el momento: {cantidad_cobrada}")
    print(f"Cantidad pendiente de cobro: {cantidad_pendiente}")

# Función principal del programa
def main():
    facturas = {}
    while True:
        print("¿Qué acción desea realizar?")
        print("1. Añadir una nueva factura")
        print("2. Pagar una factura existente")
        print("3. Terminar")
        opcion = input("Escriba el número de la acción: ")
        if opcion == "1":
            agregar_factura(facturas)
        elif opcion == "2":
            pagar_factura(facturas)
        elif opcion == "3":
            print("Terminando el programa")
            break
        else:
            print("Opción inválida")
        imprimir_cantidades(facturas)

# Llamamos a la función principal para ejecutar el programa
main()
