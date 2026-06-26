def ordenar_vuelos(vuelos):

    # Ordenar los vuelos por pasajeros (mayor a menor)
    # Si empatan, ordenar por destino alfabéticamente
    for i in range(len(vuelos)):
        for j in range(i + 1, len(vuelos)):

            if vuelos[i][3] < vuelos[j][3]:
                aux = vuelos[i]
                vuelos[i] = vuelos[j]
                vuelos[j] = aux

            elif vuelos[i][3] == vuelos[j][3]:

                if vuelos[i][1] > vuelos[j][1]:
                    aux = vuelos[i]
                    vuelos[i] = vuelos[j]
                    vuelos[j] = aux


def informe(vuelos):
    """
    Autor: Facundo Gallo
    """

    # Verificar si hay vuelos registrados
    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return 

    # Llama a la función que ordena los vuelos
    ordenar_vuelos(vuelos)

    print(4 * "--" + " INFORME GENERAL " + 4 * "--")

    # Mostrar la información de cada vuelo
    for vuelo in vuelos:
        print()
        print("Código:", vuelo[0])
        print("Destino:", vuelo[1])
        print("Horario:", vuelo[2])
        print("Pasajeros:", vuelo[3])
        print("Equipaje:", vuelo[4])
        print("Estado:", vuelo[5])
        print("Tipo:", vuelo[6])
        print()