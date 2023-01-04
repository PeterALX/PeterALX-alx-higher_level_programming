#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    rowLen = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != rowLen and rowLen != None:
            raise TypeError("Each row of the matrix must have the same size")
        if rowLen == None:
            rowLen = len(row) 
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats" )


            
    divided_mat = matrix[:]
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            divided_mat[i][j] = round(el / div, 2)
    return divided_mat 

    
