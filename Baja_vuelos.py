def verificacion_vuelos(matriz):
    #si encontrado es 1 es que no hay vuelos pre cargados y no tiene que iniciar la funcion 

    encontrado=0
    
    if len(matriz)==0:
        encontrado=1
    
    return encontrado
        
def confirmar_eliminacion(matriz, i):

    eliminar = 0

    while eliminar == 0:

        eliminar = input("desea eliminarlo? (si/no) ")
        eliminar = eliminar.lower()

        if eliminar == "si":
            matriz.pop(i)
            print()
            print("Vuelo eliminado")

        elif eliminar == "no":
            print()
            print("eliminacion cancelada")

        else:
            print()
            print("invalido, intente nuevamente")
            eliminar = 0

def buscar_vuelo(matriz, codigo):

    vuelo_encontrado = 0

    for i in range(len(matriz)):

        if matriz[i][0] == codigo:

            print("el vuelo encontrado tiene los datos {}".format(matriz[i]))
            print()

            vuelo_encontrado = 1

            if "Cancelado" in matriz[i]:
                confirmar_eliminacion(matriz, i)

            else:
                print("el estado operativo no es cancelado por eso no se puede dar de baja ese vuelo")

    return vuelo_encontrado


def baja_vuelos(matriz_vuelos):
    """
    Autor: Martin Zitola

    """
    #esta funcion elimina vuelos ya cargados

    matriz = matriz_vuelos
    salida = 0

    if verificacion_vuelos(matriz) == 1:
        print("No se pueden eliminar vuelos porque no hay ningun vuelo cargado")

    else:

        while salida != 2:

            print((4*"-") + "baja de vuelos" + (2*"-"))
            print() #para hacer un salto de linea

            codigo = input("Ingrese el codigo de vuelo que desea eliminar: ")

            vuelo_encontrado = buscar_vuelo(matriz, codigo)

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