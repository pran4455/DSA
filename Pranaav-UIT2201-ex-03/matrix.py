# -*- coding: utf-8 -*-


'''
This module provides a class used for creating a Matrix by
importing a module with a class Vector for creating vectors.
This is a part of the excercises given under the course
UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 19 2023

Revised on Wed Apr 22 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


from vector import Vector
import random


#making a class for creating a matrix
class Matrix:

    '''
    The given class stores a matrix with each row as a Vector
    object and performs functions such as addition, multiplication
    subtraction, finding determinant, finding transpose.

    The input data is not modified in any way and there are
    no side effects.

    methods:
        __init__: the constructor

        __setitem__: for setting a certain value at an index

        __getitem__: for getting a value at an index

        __len__: for finding the length of matrix

        __iter__: to create an iterable object

        __next__: to iterate through the iterable object

        __str__: for displaying class objects in human readable
        form.

        __add__: for using the '+' operation on class objects

        __sub__: for using the '-' operation on class objects

        __mul__: for using the '*' operation on class objects

        det: for finding the determinant of the matrix object

        transpose: for finding the transpose of the matrix object
    
    '''

    def __init__(self,r,c):
        self.row = r
        self.col = c
        self.mat =  [Vector(r) for x in range(c)]


    def __setitem__(self,index,val):

        '''
        Allows the matrix objects to set a value at a certain
        index.

        The input is not modified and there are no side effects.

        args:
            self: the object
            index: position at which value needs to be added
            val: the value to be added

        Returns:
            None
        
        '''

        self.mat[index[0]][index[1]] = val


    def __getitem__(self,index):

        '''
        Allows the matrix objects to get a value at a certain
        index.

        The input is not modified and there are no side effects.


        args:
            self: the object
            index: position at which value needs to be returned

        Returns:
            Value at given index.
        
        '''

        try:
            return self.mat[index[0]][index[1]]
        except Exception:
            return self.mat[index]
    

    def __len__(self):

        '''
        Returns the length of the matrix object.

        The input is not modified and there are no side effects.

        args:
            self: the object

        Returns:
            Length of matrix object.
        
        '''

        return self.col


    def __iter__(self):

        '''
        Creates an iterator object that can be used to
        iterate over.

        args:
            self: the object

        Returns:
            The object instance as an iterator object.
        
        '''

        self.current_index = 0
        return self
    

    def __next__(self):

        '''
        Returns the next item in the iteration sequence.

        Raises:
            StopIteration: If there are no more items to iterate over.

        args:
            self: the object

        Returns:
            The next item in the iteration sequence.
        
        '''

        if self.current_index >= len(self):
            raise StopIteration
        else:
            current_element = self.mat[self.current_index]
            self.current_index += 1
            return current_element    


    def __str__(self):
                
        '''
        This function takes in only the object and returns the
        given object as a str data type.

        The input is not modified in any way and there are no side
        effects

        args:
            self: the object to be displayed

        Returns:
            An object of the str data type.

        '''

        to_return = '['
        for i in range(len(self)):
            for j in range(self.row):
                to_return += str(self[i,j])
                if j != (self.row-1):
                    to_return += ','

            if i!= (self.col-1):
                to_return += '\n'
        to_return += ']'
        
        return to_return
    

    def __add__(self,other):

        '''
        This function takes in two matrices as input and calculates
        the sum of matrices and returns a matrix object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The sum of two matrices as a matrix object.
        
        '''

        if len(self) != len(other) or self.row != other.row:
            raise ValueError("Incorrect dimensions")
        
        sum_mat = Matrix(self.row, self.col)

        for i in range(len(self)):
            for j in range(self.row):
                sum_mat[i,j] = (self[i,j]+other[i,j])

        return sum_mat
    

    def __sub__(self,other):

        '''
        This function takes in two matrices as input and calculates
        the difference between the matrices and returns a matrix
        object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The difference between the two matrices as a matrix
            object.
        
        '''

        if len(self) != len(other) or self.row != other.row:
            raise ValueError("Incorrect dimensions")
        
        sub_mat = Matrix(self.row, self.col)

        for i in range(len(self)):
            for j in range(self.row):
                sub_mat[i,j] = (self[i,j]-other[i,j])

        return sub_mat
    

    def __mul__(self,other):

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

        if self.col != other.row:
            raise ValueError("The number of columns in the first matrix must be equal to the number of row in the second matrix.")
        result = Matrix(self.row, other.col)
        for i in range(result.row):
            for j in range(result.col):
                dot_product = 0
                for k in range(self.col):
                    dot_product += self[i,k] * other[k,j]
                result[i,j] = dot_product
        return result


    def det(self):

        '''
        This function takes in a matrix as input and calculates
        the determinant of the given matrix.

        The input is not modified and there are no side effects.

        args:
            self: the object

        Returns:
            The determinant of the given matrix.
        
        '''    

        if self.row != self.col:
            raise ValueError("The matrix must be square.")

        if self.row == 2:
            prod1 = self[0,0]*self[1,1]
            prod2 = self[0,1]*self[1,0]
            return prod1-prod2

        det_val = 0
        for i in range(self.col):
            sub_matrix = Matrix(self.row-1, self.col-1)
            for j in range(1, self.row):
                for k in range(self.col):
                    if k < i:
                        sub_matrix[j-1, k] = self[j, k]
                    elif k > i:
                        sub_matrix[j-1, k-1] = self[j, k]

            det_val += ((-1)**i) * self[0, i] * sub_matrix.det()

        return det_val


    def transpose(self):

        '''
        This function takes in a matrix as input and returns
        the transpose of the given matrix.

        The input is not modified and there are no side effects.

        args:
            self: the object

        Returns:
            The transpose of the given matrix.
        
        '''  

        trans_mat = Matrix(len(self),len(self[0]))
        for i in range(len(self[0])):
            for j in range(len(self)):
                trans_mat[i,j] = self[j,i]

        return trans_mat
#end of class matrix


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #generating two random matrices
    mat_1 = Matrix(4,4)
    mat_2 = Matrix(4,4)

    for i in range(4):
        for j in range(4):
            mat_1[i,j] = random.randint(-1000,1000)

    for i in range(4):
        for j in range(4):
            mat_2[i,j] = random.randint(-1000,1000)

    print(f"Matrix 1 is: \n{mat_1}\n\nMatrix 2 is: \n{mat_2}\n")

    print("Sum of matrices is:\n",mat_1 + mat_2)
    print()

    print("Difference of matrices is:\n",mat_1 - mat_2)
    print()

    print("Product of matrices is:\n",mat_1 * mat_2)
    print()

    print(f"Determinant of matrix 1 \n{mat_1}\n\n is :\n\n",mat_1.det())
    print()

    print(f"Determinant of matrix 2 \n{mat_2}\n\n is :\n\n",mat_2.det())
    print()

    print(f"Transpose of matrix 1 \n{mat_1}\n\n is :\n\n",mat_1.transpose())
    print()

    print(f"Transpose of matrix 2 \n{mat_2}\n\n is :\n\n",mat_2.transpose())
    print()