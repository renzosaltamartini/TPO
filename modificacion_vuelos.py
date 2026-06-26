def cambiar_estado(vuelos, i):
    print("1. Programado")
    print("2. Embarcando")
    print("3. En Vuelo")
    print("4. Cancelado")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vuelos[i][5] = "Programado"
    elif opcion == 2:
        vuelos[i][5] = "Embarcando"
    elif opcion == 3:
        vuelos[i][5] = "En Vuelo"
    elif opcion == 4:
        vuelos[i][5] = "Cancelado"
    else:
        print("Opción inválida")


def cambiar_tipo_vuelo(vuelos, i):
    print("1. Nacional")
    print("2. Internacional")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        vuelos[i][6] = "Nacional"
    elif opcion == 2:
        vuelos[i][6] = "Internacional"
    else:
        print("Opción inválida")


def modificar_vuelos(vuelos):

    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return vuelos

    print()
    print("---- Modificación de vuelos ----")
    print()

    codigo = input("Ingrese el código del vuelo: ")

    print("=" * 50)
    print("1. Cambiar destino")
    print("2. Cambiar horario")
    print("3. Cambiar cantidad de pasajeros")
    print("4. Cambiar equipaje")
    print("5. Cambiar estado operativo")
    print("6. Cambiar tipo de vuelo")
    print("=" * 50)

    opcion = int(input("¿Qué desea modificar?: "))

    for i in range(len(vuelos)):

        if vuelos[i][0] == codigo:

            if opcion == 1:
                vuelos[i][1] = input("Ingrese el nuevo destino (Ej: Buenos Aires): ")

            elif opcion == 2:
                vuelos[i][2] = input("Ingrese el nuevo horario (HH:MM): ")

            elif opcion == 3:
                vuelos[i][3] = int(input("Ingrese la nueva cantidad de pasajeros: "))

            elif opcion == 4:
                vuelos[i][4] = float(input("Ingrese el nuevo peso del equipaje (KG): "))

            elif opcion == 5:
                cambiar_estado(vuelos, i)

            elif opcion == 6:
                cambiar_tipo_vuelo(vuelos, i)

            else:
                print("Opción inválida")

            return vuelos

    print("No existe un vuelo con ese código")
    return vuelos