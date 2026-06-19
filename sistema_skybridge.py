import registro_vuelos
from menu import obtener_opcion_menu

def baja_vuelos(matriz_vuelos):
    """
    Autor: Martin Zitola

    """
    #esta funcion elimina vuelos ya cargados

    matriz = matriz_vuelos
    salida = 0

    while salida != 2:
        eliminar = 0
        vuelo_encontrado = 0

        print((4*"-") + "baja de vuelos" + (2*"-"))
        print() #para hacer un salto de linea

        codigo = input("Ingrese el codigo de vuelo que desea eliminar: ")

        for i in range(len(matriz)):
                
            if matriz[i][0] == codigo: #nos fijamos si esta el codigo
                print("el vuelo encontrado tiene los datos {}".format(matriz[i]))
                print()
                vuelo_encontrado = 1 #para saber si encontro el vuelo para un if afeura del for

                if "Cancelado" in matriz[i]: #nos aseguramos que el estado operativo del vuelo sea cancelado
                    while eliminar == 0:
                
                        eliminar = input("desea eliminarlo? (si/no) ")
                        eliminar = eliminar.lower() #hacemos que la variable este si o si en minuscula
                
                        if eliminar == "si":
                            matriz.pop(i) #eliminamos el dato de la matriz de un valor en especifico
                            print()
                            print("Vuelo eliminado")
                        elif eliminar == "no":
                            print()
                            print("eliminacion cancelada")
                        else:
                            print()
                            print("invalido, intente nuevamente")
                            eliminar = 0 #hace que el ciclo se siga cumpliendo para que ingrese un valor valido
                else:
                    print("el estado operativo no es cancelado por eso no se puede dar de baja ese vuelo")
        
        if vuelo_encontrado == 0:
            print()
            print("no se encontro el vuelo")

        print()
        otro_vuelo = input("desea buscar otro vuelo? si/no ")
        otro_vuelo = otro_vuelo.lower()

        if otro_vuelo == "no":
            salida = 2 #rompe el while
            print()
    
    print((4*"-")+"Fin de Baja de vuelos"+(4*"-"))
    
    return matriz


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

    print()
    print("---- Modificación de vuelos ----")
    print()

    codigo = int(input("Ingrese el código del vuelo: "))

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



def main():
    """
    Autor: Santiago Gonzalez

    """
    matriz_vuelos = []
    opcion = 0

    while opcion != 5:
        opcion = obtener_opcion_menu()

        if opcion == 1:
            matriz_vuelos = registro_vuelos.registrar_vuelos(matriz_vuelos)

        elif opcion == 2:
            matriz_vuelos = baja_vuelos(matriz_vuelos)

        elif opcion == 3:
            matriz_vuelos = modificar_vuelos(matriz_vuelos)

        elif opcion == 4:
            informe(matriz_vuelos)

    print("Programa finalizado.")

main()
