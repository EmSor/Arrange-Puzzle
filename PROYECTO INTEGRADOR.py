# J. Emilio Soriano Campos A00829390 17/10/2019

import numpy as np

#funcion que verifica si el movimiento es valido y lo hace
def juego(matrix, n): 
    vacio = [-1, -1]
    inp = [-1, -1]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == n:
                inp = [i,j]
            if matrix[i][j] == 0:
                vacio = [i,j]
    if (vacio[0] + 1 == inp[0] and vacio[1] == inp[1]) \
       or (vacio[0] - 1 == inp[0] and vacio[1] == inp[1]):  
        matrix[vacio[0]][vacio[1]] = matrix[inp[0]][inp[1]]
        matrix[inp[0]][inp[1]] = 0
    elif (vacio[0] == inp[0] and vacio[1] + 1 == inp[1]) \
         or (vacio[0] == inp[0] and vacio[1] - 1 == inp[1]):  
        matrix[vacio[0]][vacio[1]] = matrix[inp[0]][inp[1]]
        matrix[inp[0]][inp[1]] = 0
    return matrix

#funcion que imprime la primera matriz al azar
def imp_matrix():
    matrix_1 = np.arange(16)
    np.random.shuffle(matrix_1)
    matrix = np.reshape(matrix_1,(4,4))
    for ren in range(4):
        for col in range(4):
            if (len(str(matrix[ren][col])) == 1) \
               and matrix[ren][col] == 0:
                print(' ', end='   ')
            elif (len(str(matrix[ren][col])) == 1):
                print(matrix[ren][col],end='   ')
            else:
                print(matrix[ren][col], end='  ')
        print()
    return matrix

#funcion que usa la matriz ya generada para el juego
def imp_matrix_1(matrix):
    for ren in range(4): 
        for col in range(4):
            if (len(str(matrix[ren][col])) == 1) \
               and matrix[ren][col] == 0:
                print(' ', end='   ')
            elif (len(str(matrix[ren][col])) == 1):
                print(matrix[ren][col], end='   ')
            else:
                print(matrix[ren][col], end='  ')
        print()

#funcion que recibe los inputs y llama a las funciones 
def main():
    matrix = imp_matrix()
    print('\nIngrese un numero')
    n = int(input())
    print()
    while n != -1:
        matrix = juego(matrix,n)
        imp_matrix_1(matrix)
        print('\nIngrese el numero')
        n = int(input())
        print()
    print('Gracias por jugar')

main()