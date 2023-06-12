import random


def ins_sort(data):

    n = len(data)

    for i in range(1,n):

        j = i-1
        tempvar = data[i]

        while j>=0 and tempvar < data[j]:

            data[j+1] = data[j]
            j -= 1

        data[j+1] = tempvar

    return data

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

def merge(A,B):

    i = 0
    j = 0
    C = []

    while i < len(A) and j < len(B):

        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    if i < len(A):
        C.extend(A[i:])
    else:
        C.extend(B[j:])
        
    return C           

# print(merge([1,2,5,7,8,80],[-1,0,10,100]))

import ctypes

class dynarray:

    def __init__(self,val):

        if isinstance(val, int):

            self.array = self.makearray(val)
            self.top = 0
            self.size = val
        
        elif isinstance(val, list) or isinstance(val, tuple):

            self.array = self.makearray(len(val))
            for i in val:
                self.array.append(i)
            
            self.size = len(val)
            self.top = len(val) - 1
        
        else:

            raise Exception("Invalid input")
 
    def makearray(self,size):

        temp_arr = (size * ctypes.py_object)()
        return temp_arr

    def resize(self,size):

        temp = self.makearray(size)
        for i in range(self.size):
            temp[i] = self.array[i]

        self.size = size
        return temp

    def __setitem__(self,ind,ele):

        self.array[ind] = ele
    
    def append(self,ele):

        if self.size > self.top:
            self.array[self.top] = ele
            self.top += 1
        
        else:

            val = self.size * 2
            self.array = self.resize(val)
            self.array[self.top] = ele
            self.top += 1

    def __getitem__(self,ind):

        '''
        Gets the element at the specified index from the Array.

        Parameters:
        ind: The index of the element to get.

        Returns:
        The element at the specified index from the Array.
    
        '''

        return self.array[ind]

    def __str__(self):

        s = '['
        try:
            for val in self.array:

                s += str(val) + ','

            if s[-1] == ',':

                s = s[:-1]
        except:
            
            pass
        
        if s[-1] == ',':

            s = s[:-1]

        return s + ']'
    
    def isempty(self):

        pass

    def pop(self,ind=0):

        if not self.isempty():
            if ind == 0:

                pop_ele = self.array[self.top - 1]
                self.array[self.top] = ctypes.py_object
                self.top -= 1
                return pop_ele
            
            else:

                for j in range(ind,self.top - 1):

                    self.array[j] = self.array[j+1]

                print(self.top)     

            
a = dynarray(5)
a.append(103)
print(a)
a.append(203)
print(a)
a.append(3036)
print(a)
a.append(103463)
print(a)
a.append(20354)
print(a)
a.append(303)
print(a)
a.append(108)
print(a)
a.append(280)
print(a)
print(a.pop())
print(a.pop())
