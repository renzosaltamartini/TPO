import registro_vuelos

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


def modificar_vuelos (vuelos):
    """
    Autor: Facundo Gallo

    """
    # Solicita el codigo del vuelo a modificar
    codigo = input("Ingrese el código del vuelo a modificar: ")

    # Variable para indicar si se encontró el vuelo a modificar
    posicion = -1

    # Recorrer todos los vuelos 
    for i in range(len(vuelos)):
        # Verificar si el codigo ingresado coincide 
        if vuelos[i][0] == codigo:
            posicion = i

    # Si se encontro el vuelo
    if posicion != -1:
        # Pedir y guardar el nuevo destino
        vuelos[i][1] = input("Nuevo destino: ")
        # Pedir y guardar el nuevo horario
        vuelos[i][2] = input("Nuevo horario: ")
        # Pedir y guardar la nueva cantidad de pasajeros
        vuelos[i][3] = int(input("Nueva cantidad de pasajeros: "))
        # Pedir y guardar el nuevo peso de equipaje
        vuelos[i][4] = float(input("Nuevo peso de equipaje: "))
        # Pedir y guardar el nuevo estado
        vuelos[i][5] = input("Nuevo estado: ")
        # Pedir y guardar el nuevo tipo de vuelo
        vuelos[i][6] = input("Nuevo tipo de vuelo: ")
        print("Vuelo modificado exitosamente.")
    

    else:
        # Si no se encuentra el vuelo con el codigo ingresado
        print("No se encontró un vuelo con el código ingresado.")
    return vuelos

def informe(vuelos):
    """
    Autor: Facundo Gallo

    """
    # Verificar si hay vuelos registrados
    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return
    
    # Ordenar  los vulos por pasajeros (mayor a menor)
    # Si dos vuelos tienen la misma cantidad de pasajeros, 
    # los ordena alfabéticamente por destino
    else:
        for i in range(len(vuelos)):
            for j in range(i + 1, len(vuelos)):
                # Compara la cantidad de pasajeros
                if vuelos[i][3] < vuelos[j][3]:
                    # Intercambia los vuelos de posición
                    aux = vuelos[i]
                    vuelos[i] = vuelos[j]
                    vuelos[j] = aux
            
                # Si tienen la misma cantidad de pasajeros
                elif vuelos[i][3] == vuelos[j][3]:
                    # Compara los destinos alfabéticamente
                    if vuelos[i][1] > vuelos[j][1]:
                        # Intercambia los vuelos de posición
                        aux = vuelos[i]
                        vuelos[i] = vuelos[j]
                        vuelos[j] = aux
        
    print(4 * "--" + " INFORME GENERAL " + 4 * "--")
    # Recorre todos los vuelos de la lista
    for vuelo in vuelos:
        # Imprime los detalles de cada vuelo
        print()
        print("Código:", vuelo[0])
        print("Destino:", vuelo[1])
        print("Horario:", vuelo[2])
        print("Pasajeros:", vuelo[3])
        print("Equipaje:", vuelo[4])
        print("Estado:", vuelo[5])
        print("Tipo:", vuelo[6])
        print()

def menu():
    """
    Autor: Santiago Gonzalez

    No recibe parametros.
    Muestra el menú principal del sistema, solicita una opción al usuario,
    valida que esté entre las opciones permitidas y devuelve la opción elegida.

    """
    print("=" * 50)
    print("SISTEMA DE GESTIÓN: SKYBRIDGE AIRLINES")
    print("=" * 50)
    print("1. Registrar vuelo (Alta)")
    print("2. Eliminar vuelo (Baja)")
    print("3. Modificar vuelo (Modificación)")
    print("4. Informe General")
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
    matriz_vuelos = []
    opcion = 0

    while opcion != 5:
        opcion = menu()

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
