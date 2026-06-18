def mostrar_opciones_menu():
    """
    Autor: Santiago Gonzalez.
    Muestra por pantalla las opciones disponibles del menú principal.
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


def pedir_opcion_menu():
    """
    Autor: Santiago Gonzalez.
    Solicita al usuario una opción del menú principal.
    """
    opcion = input("Seleccione una opción: ")
    return opcion


def validar_opcion_menu(opcion):
    """
    Autor: Santiago Gonzalez.
    Recibe una opción y devuelve True si es numérica y está entre 1 y 5.
    """
    opcion_valida = False

    if opcion.isdigit():
        opcion = int(opcion)

        if opcion >= 1 and opcion <= 5:
            opcion_valida = True

    return opcion_valida


def obtener_opcion_menu():
    """
    Autor: Santiago Gonzalez.
    Muestra el menú, solicita una opción válida y la devuelve como entero.
    """
    mostrar_opciones_menu()
    opcion = pedir_opcion_menu()

    while not validar_opcion_menu(opcion):
        print("Opción inválida. Intente nuevamente.")
        opcion = pedir_opcion_menu()

    opcion = int(opcion)

    return opcion