def alta_vuelos():
    pass

def baja_vuelos():
    pass

def modificar_vuelos():
    pass

def informe():
    pass

def menu():
    """
    autor: Santiago Gonzalez

    Muestra el menú principal del sistema, solicita una opción al usuario,
    valida que esté entre las opciones permitidas y devuelve la opción elegida.
    
    """
    print("=" * 50)
    print("SISTEMA DE GESTIÓN: SKYBRIDGE AIRLINES")
    print("=" * 50)
    print("1. Registrar vuelo (Alta)")
    print("2. Eliminar vuelo (Baja)")
    print("3. Modificar vuelo (Modificación)")
    print("4. Informe General - Visualización de los datos")
    print("5. Salir")
    print("=" * 50)

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Opción inválida. Intente nuevamente.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    return opcion

def main():
    """
    Autor: Santiago Gonzalez

    """
    mtrz_vuelos = []
    opcion = 0

    while opcion != 5:
        opcion = menu()

        if opcion == 1:
            mtrz_vuelos = alta_vuelos(mtrz_vuelos)

        elif opcion == 2:
            mtrz_vuelos = baja_vuelos(mtrz_vuelos)

        elif opcion == 3:
            mtrz_vuelos = modificar_vuelos(mtrz_vuelos)

        elif opcion == 4:
            informe(mtrz_vuelos)

    print("Programa finalizado.")

main()