#Punto 1

def multiplicar_matrices(mat1, mat2):
    filmat1 = len(mat1)
    colmat1 = len(mat1[0])
    filmat2 = len(mat2)
    colmat2 = len(mat2[0])

    # Verificacion
    if colmat1 != filmat2:
        print("No se pueden multiplicar las matrices: número de columnas de la primera matriz no coincide con número de filas de la segunda matriz.")
        return

    # Crear matriz resultado
    matriz_resultado = [[0 for _ in range(colmat2)] for _ in range(filmat1)]

    # multiplicar matrices
    for i in range(filmat1):
        for j in range(colmat2):
            for k in range(filmat2):
                matriz_resultado[i][j] += mat1[i][k] * mat2[k][j]

    return matriz_resultado

#Sin error
a = [[1, 2, 3],
    [4, 5, 6]]

b = [[7, 8],
    [9, 10],
    [11, 12]]

matriz_resultado = multiplicar_matrices(a, b)

print(matriz_resultado)

#Con error
print("Con error")

c = [[1, 2],
    [4, 5]]

d = [[7, 8],
    [9, 10],
    [11, 12]]

matriz_resultado = multiplicar_matrices(c, d)

print(matriz_resultado)