# -*- coding: utf-8 -*-


'''
This module imports a class called point class used for
storing the coordinates of points and finding the distance
between two points. The module contains a function that can
find a specific number of points nearest to a user input point.
This is a part of the excercises given under the course UIT2201
(Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 12 2023

Revised on Wed Apr 14 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


from pointclass import point
from pointclass import point_gen
from random import randint


#function for finding a set number of nearest points
def nearest(Pnew,k,point_list):

    '''
    This function returns the required number of points
    nearest to the given point by calculating distances
    between input point and all the points in point_list
    and returns the list containing the points.

    The input is not modified and there are no side effects.

    args:
        Pnew: the point object
        k: the number of nearest elements required
        point_list: list of all the points

    Returns:
        A list of points containing k number of nearest points.
        
    '''

    distance_dict = {}

    for points in point_list:
        distance_dict[(points._x,points._y)] = Pnew.distance(points)

    items =[x for x in distance_dict.items()]  #getting key value pairs of points and distances
    distance_val = [x[1] for x in items]  #getting a list of distances

    distance_val.sort()

    count = 0  #used for getting correct index and k number of iterations
    nearest_points = []

    if len(items) > k:
        while count < k:
            for coords in items:
                if coords[1] == distance_val[count]:  #we will add the coordinates in a ordered form
                    nearest_points.append(coords)
            count+=1

    else:
        while count < len(items):
            for coords in items:
                if coords[1] == distance_val[count]:
                    nearest_points.append(coords)
            count+=1

    return nearest_points
#end of function nearest
   

#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #initializing variable for storing distances
    distances = []

    #generating n number of objects based on user input and storing in a list
    number_of_objects = int(input("Enter number of objects:"))
    point_list = point_gen(number_of_objects)

    Pnew = tuple(eval(input("Enter coordinates of point in a tuple (x,y):")))
    k = int(input("Enter number of nearest points required:"))
    print()  #for spacing

    x_coord,y_coord = Pnew
    user_point = point(x_coord,y_coord)

    for points in point_list:
        distances.append(user_point.distance(points))

    print("Points and the distances of all the points generated and input point are:")
    for index in range(len(point_list)):
        print("Point: ",(point_list[index]._x,point_list[index]._y)," Distance: ",distances[index])
    print()

    print("k number of nearest points and their distances are:")
    for points,distance in nearest(user_point,k,point_list):
        print(f"Point {points}: Distance {distance}")
    print()

    #now we will test a case where the value of required nearest numbers is greater than total number of objects
    
    test_k = 4
    test_num_objects = 3
    test_point_list = point_gen(test_num_objects)
    xcoord = randint(-1000,1000)
    ycoord = randint(-1000,1000)
    Pnew = (xcoord,ycoord)
    distances = []

    print(f"Value of k is: {test_k}\nNumber of objects generated is: {test_num_objects}")
    print(f"Randomly generated point is: {Pnew}")
    print()

    x_coord,y_coord = Pnew
    user_point = point(x_coord,y_coord)

    for points in test_point_list:
        distances.append(user_point.distance(points))

    print("Points and the distances of all the points generated and input point are:")
    for index in range(len(test_point_list)):
        print("Point: ",(test_point_list[index]._x,test_point_list[index]._y)," Distance: ",distances[index])
    print()

    print("k number of nearest points and their distances are:")
    for points,distance in nearest(user_point,test_k,test_point_list):
        print(f"Point {points}: Distance {distance}")
    print()

    #we will now test the code for a random number of points
    print("Now testing for a random number of test cases and random values of k")
    test_cases = randint(1,10)
    print(f"Number of test cases is: {test_cases}")

    for case in range(test_cases):
        distances = []

        #generating n number of objects based on randint and storing in a list
        number_of_objects = randint(4,10)
        point_list = point_gen(number_of_objects)
        Pnew = (randint(-1000,1000),randint(-1000,1000))
        k = randint(1,5)
        print()  #for spacing

        print(f"Value of k is: {k}\nNumber of objects generated is: {number_of_objects}")
        print(f"Randomly generated point is: {Pnew}")
        print()

        x_coord,y_coord = Pnew
        user_point = point(x_coord,y_coord)

        for points in point_list:
            distances.append(user_point.distance(points))

        print("Points and the distances of all the points generated and input point are:")
        for index in range(len(point_list)):
            print("Point: ",(point_list[index]._x,point_list[index]._y)," Distance: ",distances[index])
        print()

        print("k number of nearest points and their distances are:")
        for points,distance in nearest(user_point,k,point_list):
            print(f"Point {points}: Distance {distance}")
        print()
    #end of code
