# -*- coding: utf-8 -*-


def fac_find(num):

    '''
    Finds all the factors of given number.

    Input is not modified in any way and there are
    no side effects.

    args:
        num: integer value
    
    Returns:
        List of factors
    
    '''

    factors = []
    for val in range(1,num+1):
        if num % val == 0:
            factors.append(val)

    return factors


#driver code
if __name__ == '__main__':


    #complexity is O(n)
    print(fac_find(10))
