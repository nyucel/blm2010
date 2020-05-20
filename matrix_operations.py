import numpy as np
import math


def matrix_transpose(matrix: np.ndarray):

    new_matrix = np.zeros(shape=(matrix.shape[1], matrix.shape[0]), dtype=float)
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def matrix_multiplication(matrixA: np.ndarray, matrixB: np.ndarray):
    """
    Matrix multiplication
    :param matrixA: given matrix
    :param matrixB: given matrix
    :return: result matrix
    """
    if matrixA.shape[1] != matrixB.shape[0]:
        raise Exception("Matrix A colomn and Matrix B row should equal for matrix multiplication!")

    new_matrix = np.zeros(shape=(matrixA.shape[0], matrixB.shape[1]), dtype=float)
    for i in range(0, matrixA.shape[0]):
        for j in range(0, matrixB.shape[1]):
            for k in range(0, matrixA.shape[1]):
                new_matrix[i][j] += matrixA[i][k] * matrixB[k][j]
    return new_matrix


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def get_matrix_deternminant(m):
    # if matrix is 2x2
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * get_matrix_deternminant(get_matrix_minor(m, 0, c))
    return determinant


def matrix_inverse(matrix: np.ndarray):

    if matrix.shape[0] == 1:#1x1 matris için
        new_matrix = np.zeros(shape=(1, 1), dtype=float)
        new_matrix[0][0] = 1 / matrix[0][0]
        return new_matrix

    m = list()
    for i in range(matrix.shape[0]):
        rows = list()
        rows.clear()
        for j in range(matrix.shape[1]):
            rows.append(matrix[i][j])
        m.append(rows)

    determinant = get_matrix_deternminant(m)
    # 2x2 matris için
    if len(m) == 2:
        new_matrix = np.zeros(shape=(matrix.shape[0], matrix.shape[1]), dtype=float)
        new_matrix[0][0] = m[1][1] / determinant
        new_matrix[0][1] = -1 * m[0][1] / determinant
        new_matrix[1][0] = -1 * m[1][0] / determinant
        new_matrix[1][1] = m[0][0] / determinant
        return new_matrix


    cofactors = []#matrisin kofaktör hesabı
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = [list(i) for i in zip(*cofactors)]
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant

    new_matrix = np.zeros(shape=(matrix.shape[0], matrix.shape[1]), dtype=float)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            new_matrix[i][j] = cofactors[i][j]
    return new_matrix
