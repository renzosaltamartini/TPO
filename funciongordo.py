
def baja_vuelos(matriz_vuelos):
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
