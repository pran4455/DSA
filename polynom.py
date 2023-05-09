# -*- coding: utf-8 -*-

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
        for k in range(i,len(A)):
            C.append(A[k])
    else:
        for k in range(j,len(B)):
            C.append(B[k])
        
    return C

print(merge([1,5,7],[2,3,4,6,9]))