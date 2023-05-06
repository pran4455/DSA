# -*- coding: utf-8 -*-


def armstrong(num):

    '''
    Finds whether given number is an armstrong number.

    Input is not modified in any way and there are
    no side effects.

    args:
        num: integer value
    
    Returns:
        Boolean value
    
    '''

    str_num = str(num)
    raise_to = len(str_num)
    arm_val = 0
    while str_num:
        arm_val += int(str_num[-1])**raise_to
        str_num = str_num[:-1]
    
    if arm_val == num:
        return True
    
    return False


#driver code
if __name__ == '__main__':


    #complexity O(n)
    print(armstrong(31))