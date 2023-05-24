# -*- coding: utf-8 -*-

def fibonacchi(size):

    global dyn_store

    if size == 0:
        return 0
    elif size == 1:
        return 1
    elif dyn_store[size] != -1:
        return dyn_store[size]
    else:
        dyn_store[size] = fibonacchi(size-1) + fibonacchi(size-2)
        return dyn_store[size]

#driver code
if __name__ == '__main__':
    #this part of the code will only be run when the function is called directly
    #it will not be executed when it is imported as a module


    pass