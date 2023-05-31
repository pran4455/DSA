# Python3 Program for recursive binary search.


import random
import time
import datetime
import csv

# Returns index of x in arr if present, else -1
def bubble_sort(data):

	n = len(data) - 1
	for i in range(n):
		for j in range(n-i-1):
			if data[j] > data[j+1]:
				data[j],data[j+1] = data[j+1],data[j]
	return data


def sel_sort(data):

	n = len(data)
	for i in range(n):
		temp = i
		for j in range(i+1,n):
			if data[j] < data[temp]:
				temp = j
		
		if temp != i:
			data[temp], data[i] = data[i], data[temp]

	return data


def insert_sort(data):

	n = len(data)

	for i in range(1,n-1):
		j = i-1
		temp = data[i]
		while j >= 0 and data[j]>temp:
			data[j+1] = data[j]
			j -= 1
		
		data[j+1] = temp

	return data

def insert(data):
     
     n = len(data)

     for i in range(1,n-1):
          j = i-1
          temp = data[i]
          while j > 0 and data[j] > data[i]:
               data[j+1] = data[j]
               j-=1
          data[j+1] = temp

     return data

def insertion_sort(data):

    '''
    The given function sorts a given list using
    the insertion sort method and has a time complexity
    of O(n^2) and returns number of comparisons, swappings
    and amount of time taken to run the function inside
    a tuple.

    The given input is modified.

    args:
        data: the list to be sorted.

    Returns:
        A tuple containing sorted list number of comparisons,
        swappings and amount of time taken to run the function
        inside a tuple.
    
    '''

    comparisons = 0
    swappings = 0
    n = len(data)
    start_time = time.time()

    for i in range(1,n-1):

        j = i - 1
        temp_var = data[i]

        while j >= 0 and temp_var < data[j]:
                comparisons += 1
                swappings += 1
                data[j+1] = data[j]
                j-=1
        data[j+1] = temp_var

    end_time = time.time()
    time_taken = end_time - start_time

    return data
# -*- coding: utf-8 -*-


'''
This module provides a class used for creating a Vector class
Object. This is a part of the excercises given under the course
UIT2201 (Programming and Data Structures).

In this source code I have executed my own logic. The code
follows good coding practices.

Your comments and suggestions are welcome.

Created on Wed Apr 19 2023

Revised on Wed Apr 22 2023

Original Author: U. Pranaav <pranaav2210205@ssn.edu.in>

'''


import random


#making a class for creating a Vector
class Vector:

    '''
    The given class stores the coordinates of a point and
    performs functions such as finding distance between
    two points adding two points as well as subtracting
    two points.

    The input data is not modified in any way and there are
    no side effects.

    methods:
        __init__: the constructor

        __setitem__: for setting a certain value at an index

        __getitem__: for getting a value at an index

        __len__: for finding the length of matrix

        __iter__: to create an iterable object

        __next__: to iterate through the iterable object

        __add__: for using the '+' operation on class objects

        __sub__: for using the '-' operation on class objects

        __mul__: for using the '*' operation on class objects

        __str__: for displaying class objects in human readable
        form.
    
    '''

    def __init__(self,val):

        '''
        The constructor takes in two arguments and creates a
     Vector object based on the input.

        Input is not modified in any way and there are no side
        effects.

        args:
            self: the object
            val: the integer or collection using which Vector
            object is created

        Returns:
         Vector dimension variable dim and initialized Vector.

        '''

        if not isinstance(val,(int,float)):
            self.vec = val
            self.dim = len(val)
        else:
            if isinstance(val,int):
                self.vec = [0]*val
                self.dim = val
            else:
                raise ValueError("Cannot enter a float value")


    def __setitem__(self,index,val):

        '''
        Allows the Vector objects to set a value at a certain
        index.

        args:
            self: the object
            index: position at which value needs to be added
            val: the value to be added

        Returns:
            None
        
        '''

        self.vec[index] = val


    def __getitem__(self,index):

        '''
        Allows the Vector objects to get a value at a certain
        index.

        args:
            self: the object
            index: position at which value needs to be returned

        Returns:
            Value at given index.
        
        '''

        return self.vec[index]


    def __len__(self):

        '''
        Returns the length of the Vector object.

        args:
            self: the object

        Returns:
            Length of Vector object.
        
        '''
        return self.dim


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

        if self.current_index >= len(self.vec):
            raise StopIteration
        
        else:
            current_element = self.vec[self.current_index]
            self.current_index += 1
            return current_element
    

    def __add__(self,other):

        '''
        This function takes in two Vectors as input and calculates
        the sum of Vectors and returns a Vector object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The sum of two Vectors as a Vector object.
        
        '''

        if self.dim != other.dim:
            raise ValueError("Dimensions do not match")
        
        sum_vec = Vector(len(self))
        
        for i in range(len(self)):
            sum_vec[i] = (self[i]+other[i])
        
        return sum_vec
    

    def __sub__(self,other):

        '''
        This function takes in two Vectors as input and calculates
        the difference between the Vectors and returns a Vector
        object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The difference between the two Vectors as a Vector
            object.
        
        '''

        if self.dim != other.dim:
            raise ValueError("Dimensions do not match")
        
        sub_vec = Vector(len(self))
        
        for i in range(len(self)):
            sub_vec[i] = (self[i]-other[i])
        
        return sub_vec
    

    def __mul__(self,other):
                
        '''
        This function takes in two Vectors as input and calculates
        the product of the Vectors and returns a Vector object.

        The input is not modified and there are no side effects.

        args:
            self: first object
            other: second object

        Returns:
            The product of the two Vectors as a Vector object.
        
        '''

        if self.dim != other.dim:
            raise ValueError("Dimensions do not match")
        
        mul_vec = Vector(len(self))
        
        for i in range(len(self)):
            mul_vec[i] = (self[i]*other[i])

        scalar_prod = 0

        for i in mul_vec:
            scalar_prod += i

        return scalar_prod
    

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

        vec_final = '<'
        for i in range(len(self)):
            vec_final += str(self[i])
            if i != (len(self)-1):
                vec_final += ','
        return vec_final+'>'
#end of class Vector


#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module

    #generating two random vectors
    vec_1 = Vector(5)
    vec_2 = Vector(5)

    for i in range(5):
        vec_1[i] = random.randint(-1000,1000)

    for i in range(5):
        vec_2[i] = random.randint(-1000,1000)

    print(f"Vector 1 is: \n{vec_1}\nVector 2 is: \n{vec_2}\n")

    print("Sum of vectors is:\n",vec_1 + vec_2)
    print()  #for spacing between lines

    print("Difference of vectors is:\n",vec_1 - vec_2)
    print()

    print("Scalar product of vectors is:\n",vec_1 * vec_2)
    print()

    print(f"Length of vector 1 \n{vec_1}\n is: ",len(vec_1))
    print()

    print(f"Length of vector 2 \n{vec_2}\n is: ",len(vec_2))
    print()

def merg(a,b):

	i = 0
	j = 0
	res_l = []
	
	while i < len(a) and j < len(b):
		
		if a[i] < b[j]:
			res_l.append(a[i])
			i += 1
		else:
			res_l.append(b[j])
			j += 1
	
	if j < len(b):
		res_l.extend(b[j:])
	else:
		res_l.extend(a[i:])

	return res_l

print(merg([5,7,9,10,99],[2,4,6,11,34]))

def merge_sort(data):
    if len(data) > 1:
        m = len(data) // 2
        l_s = data[:m]
        r_s = data[m:]
        return merg(merge_sort(l_s), merge_sort(r_s))
    else:
	    return data
	
def mer(a,b):
    i = 0
    j = 0
    c = []
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        
        else:
            c.append(b[j])
            j += 1
        
    if i < len(a):
        c.extend(a[i:])

    else:
        c.extend(b[j])

def mersor(data):

    if len(data) > 1:
        m = len(data) // 2
        l_s = data[:m]
        r_s = data[m:]
        return merg(merge_sort(l_s), merge_sort(r_s))
    else:
	    return data

def par(data):
    i = 0
    j = len(data) - 2
    pivot = data[len(data)-1]
     
    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        
        if i>=j:
            break

        data[i] , data[j] = data[j] , data[i]
        j -= 1
        i += 1

    data[i] , data[len(data)-1] = data[len(data)-1] , data[i]
        

def getmid_index(arr, left, right):
    mid = (left + right) // 2
    if arr[left] <= arr[mid] <= arr[right] or arr[right] <= arr[mid] <= arr[left]:
        return mid
    elif arr[mid] <= arr[left] <= arr[right] or arr[right] <= arr[left] <= arr[mid]:
        return left
    else:
        return right


def partition(data,i,j,pivot):
        while True:
            while i <= j and data[i] < pivot:
                i+=1
            while i<= j and data[j] > pivot:
                j-=1
            if i>=j:
                break
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        data[i], data[len(data)-1] = data[len(data)-1], data[i]
        return i


def quicksort(data):
    if len(data) > 1:
        pivot_ind = getmid_index(data,0,len(data)-1)
        pivot = data[pivot_ind]
        data[pivot_ind], data[len(data)-1] = data[len(data)-1], data[pivot_ind]

        i = 0
        j = len(data) - 2
        i = partition(data,i,j,pivot)
        return quicksort(data[:i]) + [pivot] + quicksort(data[i+1:])
    else:
        return data


def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

		
def random_list(size):

    '''
    The given function generates a random number of values
    and returns the values in a list.

    args:
        size: the number of point objects to be
        generated

    Returns:
        A list of random integer values.
    
    '''

    random_list = []

    for case in range(size):
        x_val = random.randint(-1000,1000)
        random_list.append(x_val)   

    return random_list  
    
# Driver Code
if __name__ == '__main__':
    with open('write.csv', 'w') as f:
        a = Vector(5)
        writer = csv.writer(f)
        writer.writerow(a)