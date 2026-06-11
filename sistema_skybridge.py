
def registrar_vuelos(matriz_vuelos):
    """
    Autor: Renzo Saltamartini

    """

    n = 0
    
    while n >= 0:

        vuelo = [] # SE LIMPIA CADA VEZ QUE SE REGISTRA UN NUEVO VUELO

        print(f"{4 * "--"} {"REGISTRO DE VUELOS: SKYBRIDGE AIRLINES"} {4 * "--"}")
        print("Bienvenid@, completa los datos para registrar el vuelo correctamente.")

        print()
        print(f"{"1/7"} {2 * "--"} {"CODIGO"} {2 * "--"}")
        print("4 - 10 CARACTERES Y ALFANUMERICO")
        print()
        codigo = input("Ingrese el codigo de vuelo: ")

        while len(codigo) < 4 or len(codigo) > 10 or not codigo.isalnum() or not any(c.isdigit() for c in codigo):
            if len(codigo) < 4 or len(codigo) > 10:
                print("El codigo debe tener entre 4 y 10 caracteres.")
            elif not codigo.isalnum():
                print("El codigo debe ser alfanumerico, sin espacios ni simbolos.")
            elif not any(c.isdigit() for c in codigo):
                print("El codigo debe contener al menos un numero.")
            codigo = input("Ingrese el codigo de vuelo: ")

        codigos_existentes = [v[0] for v in matriz_vuelos] # BUSCA EN LA LISTA vuelos PARTIENDO DESDE LA PRIMER LISTA Y CON EL SUB-INDICE 0
                                                    # YA QUE AHI SE ENCUENTRAN LOS CODIGOS
        while codigo in codigos_existentes:
            print("Ese codigo ya existe, ingrese uno diferente.")
            codigo = input("Ingrese el codigo de vuelo: ")

            while len(codigo) < 4 or len(codigo) > 10 or not codigo.isalnum() or not any(c.isdigit() for c in codigo):
                if len(codigo) < 4 or len(codigo) > 10:
                    print("El codigo debe tener entre 4 y 10 caracteres.")
                elif not codigo.isalnum():
                    print("El codigo debe ser alfanumerico, sin espacios ni simbolos.")
                elif not any(c.isdigit() for c in codigo):
                    print("El codigo debe contener al menos un numero.")

                codigo = input("Ingrese el codigo de vuelo: ")

            codigos_existentes = [v[0] for v in matriz_vuelos]

        # LO QUE HACE LA FUNCION ANY, ES QUE DETECTA SI AL MENOS (ANY = AL MENOS) HAY UN DIGITO EN EL CODIGO: codigo

        print(f"El codigo: {codigo}, fue registrado exitosamente.")
        vuelo.append(codigo)

        print()
        print(f"{"2/7"} {2 * "--"} {"DESTINO"} {2 * "--"}")
        print()
        destino = input("Ingrese el destino del vuelo, ejemplo (Buenos Aires): ")
        while len(destino) == 0:
            print("Debes ingresar un destino")
            destino = input("Ingrese el destino del vuelo, ejemplo (Buenos Aires): ")
        print(f"El destino: {destino} fue registrado.")
        vuelo.append(destino)

        print()
        print(f"{"3/7"} {2 * "--"} {"HORARIO"} {2 * "--"}")
        print()
        horario = input("Ingrese el horario, respeta (HH:MM): ")
        while len(horario) != 5 or horario[2] != ":" or not horario[0:2].isdigit() or not horario[3:5].isdigit():
            print("Formato invalido, ejemplo: 08:30")
            horario = input("Ingrese el horario, respeta (HH:MM): ")

        while int(horario[0:2]) > 23 or int(horario[3:5]) > 59:
            print("Formato invalido, ejemplo: 08:30")
            horario = input("Ingrese el horario, respeta (HH:MM): ")
            while len(horario) != 5 or horario[2] != ":" or not horario[0:2].isdigit() or not horario[3:5].isdigit():
                print("Formato invalido, ejemplo: 08:30")
                horario = input("Ingrese el horario, respeta (HH:MM): ")
        print(f"El horario: {horario} fue registrado.")
        vuelo.append(horario)

        print()
        print(f"{"4/7"} {2 * "--"} {"PASAJEROS"} {2 * "--"}")
        print()
        pasajeros = input("Ingrese la cantidad de pasajeros: ")
        while not pasajeros.isdigit() or int(pasajeros) < 0:
            print("El ingreso de pasajeros esta mal.")
            pasajeros = input("Ingrese la cantidad de pasajeros: ")
        pasajeros = int(pasajeros)
        print(f"El total de pasajeros: {pasajeros} fue registrado.")
        vuelo.append(pasajeros)

        print()
        print(f"{"5/7"} {2 * "--"} {"PESO"} {2 * "--"}")
        print()
        peso = float(input("Ingrese el peso(kg) exacto del equipaje: "))
        while peso < 0:
            print("El peso debe ser mayor a 0")
            peso = float(input("Ingrese el peso(kg) exacto del equipaje: "))
        print(f"El peso total: {peso}kg fue registrado.")
        vuelo.append(peso)

        print()
        print(f"{"6/7"} {2 * "--"} {"ESTADO OPERATIVO"} {2 * "--"}")
        print()
        print(f">>> 1.   Programado")
        print(f">>> 2.   Embarcando")
        print(f">>> 3.   En Vuelo")
        print(f">>> 4.   Cancelado")
        opcion_operativo = input("Selecciona la opcion del 1 al 4: ")
        while not opcion_operativo.isdigit() or int(opcion_operativo) < 1 or int(opcion_operativo) > 4:
            print("La opcion es incorrecta, debe ser del 1 al 4")
            opcion_operativo = input("Selecciona la opcion del 1 al 4: ")
        opcion_operativo = int(opcion_operativo)
        if opcion_operativo == 1:
            estado_operativo = "Programado"
        elif opcion_operativo == 2:
            estado_operativo = "Embarcando"
        elif opcion_operativo == 3:
            estado_operativo = "En vuelo"
        else:
            estado_operativo = "Cancelado"
        print(f"El estado operativo del vuelo: {estado_operativo} fue registrado.")
        vuelo.append(estado_operativo)

        print()
        print(f"{"7/7"} {2 * "--"} {"TIPO"} {2 * "--"}")
        print()
        print(f">>> 1.   Nacional")
        print(f">>> 2.   Internacional")
        opcion_vuelo = input("Selecciona la opcion 1 o 2: ")
        while not opcion_vuelo.isdigit() or int(opcion_vuelo) < 1 or int(opcion_vuelo) > 2:
            print("La opcion es incorrecta, debe ser 1 o 2")
            opcion_vuelo = input("Selecciona la opcion 1 o 2: ")
        opcion_vuelo = int(opcion_vuelo)
        if opcion_vuelo == 1:
            tipo_vuelo = "Nacional"
        else:
            tipo_vuelo = "Internacional"
        print(f"El tipo de vuelo: {tipo_vuelo} fue registrado.")
        vuelo.append(tipo_vuelo)

        print()
        print(f"{2 * "--"} {"VUELO REGISTRADO"} {2 * "--"}")
        print(f"El vuelo con el codigo: {codigo} fue registrado exitosamente.") # TERMINA EL REGISTRO DE VUELO
        matriz_vuelos.append(vuelo) # SE AGREGA LA LISTA CREADA DE ESTE VUELO A LA LISTA DE TODOS LOS VUELOS

        print()
        print(f"{4 * "--"} {"¿REGISTRAR OTRO VUELO?"} {4 * "--"}")
        print(f">>> Si:   1")
        print(f">>> No:   -1")
        n = input("Elegi la opcion 1(si) o -1(no): ")
        while n != "1" and n != "-1":
            print("La opcion es incorrecta, debe ser -1 o 1")
            n = input("Elegi la opcion 1(si) o -1(no): ")
        n = int(n)
        if n == -1:
            print(f"{4 * "--"} {"SKYBRIDGE AIRLINES"} {4 * "--"}")
            print("Registro de vuelos finalizado.")

    return matriz_vuelos

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
        
    print(4 * "--" + " IFORME GENERAL " + 4 * "--")
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
            matriz_vuelos = registrar_vuelos(matriz_vuelos)

        elif opcion == 2:
            matriz_vuelos = baja_vuelos(matriz_vuelos)

        elif opcion == 3:
            matriz_vuelos = modificar_vuelos(matriz_vuelos)

        elif opcion == 4:
            informe(matriz_vuelos)

    print("Programa finalizado.")

main()
