#Punto 3


def cargar_votos():
    candidatos = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre del candidato {i+1}: ")
        municipios = []
        for j in range(5):
            municipio = input(f"Ingrese el nombre del municipio {j+1}: ")
            votos = int(input(f"Ingrese la cantidad de votos obtenidos por {nombre} en {municipio}: "))
            municipios.append([municipio, votos])
        candidatos.append([nombre, municipios])
    return candidatos


def imprimir_votos_candidato(candidatos):
    nombre = input("Ingrese el nombre del candidato: ")
    for candidato in candidatos:
        if candidato[0] == nombre:
            total_votos = sum([municipio[1] for municipio in candidato[1]])
            print(f"El total de votos obtenidos por {nombre} es: {total_votos}")
            return
    print(f"No se encontró al candidato {nombre} en la lista.")


def imprimir_votos_municipio(candidatos):
    municipio = input("Ingrese el nombre del municipio: ")
    total_votos = 0
    for candidato in candidatos:
        for municipio_votos in candidato[1]:
            if municipio_votos[0] == municipio:
                total_votos += municipio_votos[1]
                break
    if total_votos > 0:
        print(f"El total de votos en {municipio} es: {total_votos}")
    else:
        print(f"No se encontró el municipio {municipio} en la lista.")


def imprimir_ganador(candidatos):
    total_votos = [sum([municipio[1] for municipio in candidato[1]]) for candidato in candidatos]
    ganador = candidatos[total_votos.index(max(total_votos))][0]
    print(f"El candidato ganador es: {ganador}")


# Cargar los votos obtenidos por cada candidato en cada municipio
candidatos = cargar_votos()

# Imprimir el total de votos de un candidato solicitado
imprimir_votos_candidato(candidatos)

# Imprimir el total de votos en un municipio solicitado
imprimir_votos_municipio(candidatos)

# Imprimir el candidato ganador
imprimir_ganador(candidatos)