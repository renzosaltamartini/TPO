vuelos = []

# PARA CREAR UN VUELO DESDE OTRO ARCHIVO, ejemplo:
# vuelo = function.registrar_vuelos()

def registrar_vuelos():

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

        codigos_existentes = [v[0] for v in vuelos] # BUSCA EN LA LISTA vuelos PARTIENDO DESDE LA PRIMER LISTA Y CON EL SUB-INDICE 0
                                                    # YA QUE AHI SE ENCUENTRAN LOS CODIGOS
        while codigo in codigos_existentes:
            print("Ese codigo ya existe, ingrese uno diferente.")
            codigo = input("Ingrese el codigo de vuelo: ")
            codigos_existentes = [v[0] for v in vuelos]

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
        pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
        while pasajeros < 0:
            print("No pueden haber 0 pasajeros")
            pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
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
        opcion_operativo = int(input("Selecciona la opcion del 1 al 4: "))
        while opcion_operativo < 1 or opcion_operativo > 4:
            print("La opcion es incorrecta, debe ser del 1 al 4")
            opcion_operativo = int(input("Selecciona la opcion del 1 al 4: "))
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
        opcion_vuelo = int(input("Selecciona la opcion 1 o 2: "))
        while opcion_vuelo < 1 or opcion_vuelo > 2:
            print("La opcion es incorrecta, debe ser 1 o 2")
            opcion_vuelo = int(input("Selecciona la opcion 1 o 2: "))
        if opcion_vuelo == 1:
            tipo_vuelo = "Nacional"
        else:
            tipo_vuelo = "Internacional"
        print(f"El tipo de vuelo: {tipo_vuelo} fue registrado.")
        vuelo.append(tipo_vuelo)

        print()
        print(f"{2 * "--"} {"VUELO REGISTRADO"} {2 * "--"}")
        print(f"El vuelo con el codigo: {codigo} fue registrado exitosamente.") # TERMINA EL REGISTRO DE VUELO
        vuelos.append(vuelo) # SE AGREGA LA LISTA CREADA DE ESTE VUELO A LA LISTA DE TODOS LOS VUELOS

        print()
        print(f"{4 * "--"} {"¿REGISTRAR OTRO VUELO?"} {4 * "--"}")
        print(f">>> Si:   1")
        print(f">>> No:   -1")
        n = int(input("Elegi la opcion 1(si) o -1(no): "))
        while n != 1 and n != -1:
            print("La opcion es incorrecta, debe ser -1 o 1")
            n = int(input("Elegi la opcion 1(si) o -1(no): "))
        
        if n == -1:
            print(f"{4 * "--"} {"SKYBRIDGE AIRLINES"} {4 * "--"}")
            print("Registro de vuelos finalizado.")

    return vuelos
