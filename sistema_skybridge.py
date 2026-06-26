import registro_vuelos
from menu import obtener_opcion_menu
from Baja_vuelos import baja_vuelos
from modificacion_vuelos import modificar_vuelos
from informe import informe




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
