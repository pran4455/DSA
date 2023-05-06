# -*- coding: utf-8 -*-


def matrix_mul(matrix_1,matrix_2):

    '''
        This function takes in two matrices as input and calculates
        the product of the matrices and returns a matrix object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The product of the two matrices as a matrix object.
        
    '''     

    if len(matrix_1) != len(matrix_2[0]):
        raise ValueError("The number of columns in the first matrix must be equal to the number of row in the second matrix.")
    result = [[0 for x in range(len(matrix_1[0]))] for j in range(len(matrix_2))]
    for i in range(len(result[0])):
        for j in range(len(result)):
            dot_product = 0
            for k in range(len(matrix_1)):
                dot_product += matrix_1[i][k] * matrix_2[k][j]
            result[i][j] = dot_product
    return result

if __name__ == '__main__':


    #time complexity: O(n^3)
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3],[4,5,6],[7,8,9]]

    print(matrix_mul(m1,m2))
