'''Verificar si hay vuelos cargados.
Si no hay, mostrar: "No hay vuelos registrados".
Ordenar los vuelos:
De mayor a menor cantidad de pasajeros.
Si dos tienen la misma cantidad de pasajeros, ordenar por destino alfabéticamente.
Recorrer la lista de vuelos con un for.
Mostrar los datos de cada vuelo:
Código
Destino
Horario
Pasajeros
Equipaje
Estado
Tipo
Eso es todo. El objetivo es mostrar todos los vuelos ordenados correctamente.'''

def informe(vuelos):
    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return
    
    # Ordenar por pasajeros (mayor a menor)
    # Si empatan, por destino (alfabéticamente)
    for i in range(len(vuelos)):
        for j in range(i + 1, len(vuelos)):
            if vuelos[i][3] < vuelos[j][3]:
                aux = vuelos[i]
                vuelos[i] = vuelos[j]
                vuelos[j] = aux
            
            elif vuelos[i][3] == vuelos[j][3]:
                if vuelos[i][1] > vuelos[j][1]:
                    aux = vuelos[i]
                    vuelos[i] = vuelos[j]
                    vuelos[j] = aux
    
    print("IFORME GENERAL")

    for vuelo in vuelos:
        print("Código:", vuelo[0])
        print("Destino:", vuelo[1])
        print("Horario:", vuelo[2])
        print("Pasajeros:", vuelo[3])
        print("Equipaje:", vuelo[4])
        print("Estado:", vuelo[5])
        print("Tipo:", vuelo[6])
        print()

def main():
    vuelos = [
        ["SB101", "Madrid", "14:30", 150, 5200.5, "Programado", "Internacional"],
        ["SB102", "Miami", "10:00", 300, 4500.0, "En vuelo", "Internacional"],
        ["SB103", "Buenos Aires", "09:00", 300, 3800.0, "Programado", "Nacional"],
        ["SB104", "Santiago", "16:45", 200, 4100.0, "Embarcando", "Internacional"]
    ]
    informe(vuelos)

main()