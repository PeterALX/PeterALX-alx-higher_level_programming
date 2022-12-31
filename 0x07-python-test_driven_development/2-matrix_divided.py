#!/usr/bin/python3

def matrix_divided(matrix, div):
    divided_mat = matrix[:]
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            divided_mat[i][j] = el / 2
    return divided_mat 

    
