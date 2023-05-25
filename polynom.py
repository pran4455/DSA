# Python3 Program for recursive binary search.


import random
import time
import datetime

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
    current_time = datetime.datetime.time()
    print(current_time)