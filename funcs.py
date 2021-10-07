from itertools import count
import random
import time
from alive_progress import alive_bar

def create_random_array(size: int):
    '''
    create random array of size (2**size) elements
    '''
    start = time.time()
    arr = []
    with alive_bar(2**size) as bar:
        for i in range(2**size):
            arr.append(random.randint(1, 100000))
            bar()
    print("arr length :",  len(arr))
    print("time to create array :", time.time() - start)
    return arr


def create_sorted_array(size: int):
    '''
    create random sorted array of size (2**size) elements
    '''
    start = time.time()
    arr = []
    with alive_bar(2**size) as bar:
        for i in range(2**size):
            arr.append(random.randint(1, 100000))
            bar()
    arr = sorted(arr)
    print("arr length :",  len(arr))
    print("time to create array :", time.time() - start)
    return arr


def create_inverted_sorted_array(size: int):
    '''
    create random inverted sorted array of size (2**size) elements
    '''
    start = time.time()
    arr = []
    with alive_bar(2**size) as bar:
        for i in range(2**size):
            arr.append(random.randint(1, 100000))
            bar()
    arr = sorted(arr, key=lambda x: 1/x)
    print("arr length :",  len(arr))
    print("time to create array :", time.time() - start)
    return arr


def create_random_array_123(size: int):
    '''
    create random array of size (2**size)
    only 1, 2, and 3 can appear in this array
    '''
    start = time.time()
    arr = []
    with alive_bar(2**size) as bar:
        for i in range(2**size):
            arr.append(random.randint(1, 3))
            bar()
    print("arr length :",  len(arr))
    print("time to create array :", time.time() - start)
    return arr


def selection_sort(arr: list):
    '''
    sort an array using selection sort
    '''
    counter = 0
    start = time.time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            counter += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    timee = time.time() - start
    print(counter)
    return arr, counter, timee


def insertion_sort(arr: list):
    '''
    sort an array using insertion sort
    '''
    start = time.time()
    counter = 0
    for i in range(1, len(arr)):
        counter += 1
        j = i - 1
        key = arr[i]
        while j >= 0:
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                counter += 1
            else:
                counter += 1
                break
        arr[j+1] = key
    timee = time.time() - start
    return arr, counter, timee


def calculate_time_for_merge_sort(arr: list):
    '''
    calculate time to sort array using merge sort
    help function to avoid calculating time for each recursion call of mergesort
    '''
    start = time.time()
    arr, counter = merge_sort(arr, 0)
    timee = time.time() - start
    return arr, counter, timee


def merge_sort(arr: list, counter: int = 0):
    '''
    sort an array using merge sort
    '''
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        L, counter = merge_sort(L, counter)
        R, counter = merge_sort(R, counter)
  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            counter += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr, counter


def shell_sort(arr: list):
    '''
    sort an array using shell sort
    '''
    counter = 0
    start = time.time()
    leng = len(arr)
    i = 1
    while (i < leng/3):
        i = 3*i + 1

    while (i >= 1):
        for j in range(i, leng):
            k = j
            while k >= i:
                if (arr[k] < arr[k-i]):
                    counter += 1
                    arr[k], arr[k-i] = arr[k-i], arr[k]
                    k -= i
                else:
                    counter += 1
                    break
        i = i // 3

    timee = time.time() - start
    return arr, counter, timee


if __name__ == "__main__":
    arr, counter, timee = insertion_sort(create_random_array(15))
    print(timee)
    print(arr[0:100])