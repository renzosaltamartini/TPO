def menu():

    print("=" * 50)
    print("SISTEMA DE GESTIÓN: SKYBRIDGE AIRLINES")
    print("=" * 50)
    print("1. Registrar vuelo (Alta)")
    print("2. Eliminar vuelo (Baja)")
    print("3. Modificar vuelo (Modificación)")
    print("4. Informe General - Visualización de los datos")
    print("5. Salir")
    print("=" * 50)

    opcion = int(input("Seleccione una opción: "))

    while opcion < 1 or opcion > 5 :
        print("Opción inválida. Intente nuevamente.")
        opcion = int(input("Seleccione una opción: "))

    return opcion



def main():

    opcion = menu()


    

main()