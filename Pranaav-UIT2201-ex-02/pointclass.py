# -*- coding: utf-8 -*-


'''
This module provides a class used for storing the coordinates of
points and the stored data can be used to find the distance
between two points. This is a part of the excercises given under
the course UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 12 2023

Revised on Wed Apr 14 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import random


class point:

    '''
    The given class stores the coordinates of a point and
    performs functions such as finding distance between
    two points adding two points as well as subtracting
    two points.

    The input data is not modified in any way and there are
    no side effects.

    methods:
        __init__: the constructor

        __add__: for using the '+' operation on class objects

        __sub__: for using the '-' operation on class objects

        __str__: for displaying class objects in human readable
        form.

        distance: for calculating distance between two point
        objects
    
    '''

    __slots__ = ('_x', '_y')  #setting the variables so that we can optimize memory usage


    def __init__(self,x_coord,y_coord):

        '''
        The constructor here takes in 3 arguments, and assigns
        the values of x coordinates and y coordinates to special
        variables _x and _y which are used for performing other
        functions.

        The input is not modified and there are no side effects.

        args:
            self: the object
            x_coord: value of x coordinate
            y_coord: value of y coordinate

        returns:
            variables _x and _y used in other functions in class.
        
        '''

        self._x = x_coord
        self._y = y_coord


    def __add__(self,other):
    
        '''
        This function takes in two points as input and calculates
        the sum of each point's x coordinates and each point's y
        coordinates and returns a point with the calculated x and
        y coordinates.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The sum of coordinates of two points.
        
        '''

        return point(self._x+other._x,self._y+other._y)


    def __sub__(self,other):
       
        '''
        This function takes in two points as input and calculates
        the difference of each point's x coordinates and each point's y
        coordinates and returns a point with the calculated x and
        y coordinates.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The difference of coordinates of two points.
        
        '''

        return point(self._x-other._x,self._y-other._y)


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

        return f'({self._x},{self._y})'
    
    
    def distance(self,other):

        '''
        This function takes in two points as input and calculates
        the distance between them.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The distance between the two points.
        
        '''

        x_diff = (self._x-other._x)**2
        y_diff = (self._y-other._y)**2
        return (x_diff + y_diff)**0.5
#end of class point


#defining a function for generating a random number of point objects
def point_gen(point_count):

    '''
    The given function generates a random number of point
    objects and returns them as a list of point objects.

    args:
        point_count: the number of point objects to be
        generated

    Returns:
        A list of point objects.
    
    '''

    point_list = []
    for case in range(point_count):
        x_val = random.randint(-1000,1000)
        y_val = random.randint(-1000,1000)
        point_1 = point(x_val,y_val)  #creating a new object each iteration
        point_list.append(point_1)   

    return point_list         
#end of function point_gen


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #initializing variable for storing distances
    distances = []

    #generating n number of objects based on user input and storing in a list
    number_of_objects = int(input("Enter number of objects:"))
    point_list = point_gen(number_of_objects)

    input_point = tuple(eval(input("Enter coordinates of point in a tuple (x, y):")))
    print()  #for spacing between lines

    #setting the user input point as an object of class point
    x_coord,y_coord = input_point
    user_point = point(x_coord,y_coord)

    for points in point_list:
        distances.append(user_point.distance(points))

    print("Points and the distances of all the points generated and input point are:")
    for index in range(len(point_list)):
        print("Point: ",(point_list[index]._x,point_list[index]._y)," Distance: ",distances[index])
    print()

    #testing the addition, subtraction operations on points
    point_1 = point(5,10)
    point_2 = point(6,12)

    print(f"Point 1 is: {point_1} and Point 2 is: {point_2}")
    print("Sum of both points is:",point_1 + point_2)
    print("Difference between both points is:",point_1 - point_2)
    print()
    #end of code
