#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
    matrix (list[[list]]): a matrix
    """
    matrix_copy = [[matrix[i][j] for j in range(0,
                                                len(matrix[i]))] for i in range(0,
                                                                                len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix_copy[len(matrix) - j - 1][i]
