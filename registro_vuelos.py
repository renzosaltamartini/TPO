def pedir_codigo(matriz_vuelos):

    print()
    print(f"{"1/7"} {2 * "--"} {"CODIGO"} {2 * "--"}")
    print("4 - 10 CARACTERES Y ALFANUMERICO")
    print()

    codigo = input("Ingrese el codigo de vuelo: ")

    digitos = 0
    for c in codigo:
        if c.isdigit():
            digitos += 1

    while len(codigo) < 4 or len(codigo) > 10 or not codigo.isalnum() or digitos == 0:
        if len(codigo) < 4 or len(codigo) > 10:
            print("El codigo debe tener entre 4 y 10 caracteres.")
        elif not codigo.isalnum():
            print("El codigo debe ser alfanumerico, sin espacios ni simbolos.")
        elif digitos == 0:
            print("El codigo debe contener al menos un numero.")

        codigo = input("Ingrese el codigo de vuelo: ")

        digitos = 0
        for c in codigo:
            if c.isdigit():
                digitos += 1

    codigos_existentes = []
    a = 0
    for i in matriz_vuelos:
        if matriz_vuelos[a][0]:
            codigos_existentes.append(matriz_vuelos[a][0])
        a += 1

    while codigo in codigos_existentes:
        print("Ese codigo ya existe, ingrese uno diferente.")
        codigo = input("Ingrese el codigo de vuelo: ")

        digitos = 0
        for c in codigo:
            if c.isdigit():
                digitos += 1

        while len(codigo) < 4 or len(codigo) > 10 or not codigo.isalnum() or digitos == 0:
            if len(codigo) < 4 or len(codigo) > 10:
                print("El codigo debe tener entre 4 y 10 caracteres.")
            elif not codigo.isalnum():
                print("El codigo debe ser alfanumerico, sin espacios ni simbolos.")
            elif digitos == 0:
                print("El codigo debe contener al menos un numero.")

            codigo = input("Ingrese el codigo de vuelo: ")

            codigos_existentes = []
            a = 0
            for i in matriz_vuelos:
                if matriz_vuelos[a][0]:
                    codigos_existentes.append(matriz_vuelos[a][0])
                a += 1

    print(f"El codigo: {codigo}, fue registrado exitosamente.")

    return codigo

def pedir_destino():
    print()
    print(f"{"2/7"} {2 * "--"} {"DESTINO"} {2 * "--"}")
    print()
    destino = input("Ingrese el destino del vuelo, ejemplo (Buenos Aires): ")
    while len(destino) == 0:
        print("Debes ingresar un destino")
        destino = input("Ingrese el destino del vuelo, ejemplo (Buenos Aires): ")
    print(f"El destino: {destino} fue registrado.")

    return destino

def pedir_horario():
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

    return horario

def pedir_pasajeros():
    print()
    print(f"{"4/7"} {2 * "--"} {"PASAJEROS"} {2 * "--"}")
    print()
    pasajeros = input("Ingrese la cantidad de pasajeros: ")
    while not pasajeros.isdigit() or int(pasajeros) < 0:
        print("El ingreso de pasajeros esta mal.")
        pasajeros = input("Ingrese la cantidad de pasajeros: ")
    pasajeros = int(pasajeros)
    print(f"El total de pasajeros: {pasajeros} fue registrado.")

    return pasajeros

def pedir_peso():
    print()
    print(f"{"5/7"} {2 * "--"} {"PESO"} {2 * "--"}")
    print()
    peso = float(input("Ingrese el peso(kg) exacto del equipaje: "))
    while peso < 0:
        print("El peso debe ser mayor a 0")
        peso = float(input("Ingrese el peso(kg) exacto del equipaje: "))
    print(f"El peso total: {peso}kg fue registrado.")

    return peso

def pedir_estado():
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

    return estado_operativo

def pedir_tipo():
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

    return tipo_vuelo

def registrar_vuelos(matriz_vuelos):
    """
    Autor: Renzo Saltamartini

    """

    n = 0
    
    while n >= 0:

        vuelo = [] # SE LIMPIA CADA VEZ QUE SE REGISTRA UN NUEVO VUELO

        print(f"{4 * "--"} {"REGISTRO DE VUELOS: SKYBRIDGE AIRLINES"} {4 * "--"}")
        print("Bienvenid@, completa los datos para registrar el vuelo correctamente.")

        codigo = pedir_codigo(matriz_vuelos)
        destino = pedir_destino()
        horario = pedir_horario()
        pasajeros = pedir_pasajeros()
        peso = pedir_peso()
        estado_operativo = pedir_estado()
        tipo_vuelo = pedir_tipo()

        vuelo.append(codigo)
        vuelo.append(destino)
        vuelo.append(horario)
        vuelo.append(pasajeros)
        vuelo.append(peso)
        vuelo.append(estado_operativo)
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
            print(matriz_vuelos)
            print(codigos_existentes)

    return matriz_vuelos