vuelos = []

def registrar_vuelos():
    codigo = input("Ingrese el codigo de vuelo: ")
    print("Recorda que debe tener entre 4-10 caracteres y es alfanumerico")
    
    if len(codigo) < 4 or len(codigo) > 10:
        print("El código debe tener entre 4 y 10 caracteres")

    elif not codigo.isalnum():
        print("El código debe ser alfanumérico")

    elif codigo in vuelos:
        print("Ese código ya existe")

    else:
        vuelos.append(codigo)
        print("Código registrado")

    destino = input("Ingrese el destino del vuelo, ejemplo (Buenos Aires): ")
    horario = input("Ingrese el horario, respeta (HH:MM): ")
    while horario[2] != ":" or not horario[0:2].isdigit() or not horario[3:5].isdigit():
        print("Error: formato inválido. Ejemplo: 08:30")
        horario = input("Ingrese el horario, respeta (HH:MM): ")

#registrar_vuelos()