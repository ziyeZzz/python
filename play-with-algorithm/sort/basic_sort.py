#O(n^2)
import time

a = [6,4,5,3.1,2,1]
def decorator(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        print(args[0]+':'+str(end_time-start_time))
    return wrapper

@decorator
def selectionSortQuick(name, arr):
    for i in range(len(arr)):
        mini = min(arr[i:])
        mini_index = arr[i:].index(mini)
        arr[i+mini_index] = arr[i]
        arr[i] = mini
    # print(arr)

@decorator
def selectionSort(name, arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
           if(arr[j]<arr[min_index]):
               min_index = j
        arr = swap(arr, i, min_index)
    # print(arr)
def swap(arr, i, j):
    i_value = arr[i]
    arr[i] = arr[j]
    arr[j] = i_value
    return arr

# b=['a','z','v']
# name = 'selectionSort'
# selectionSort(name,a)

# student = [('A',60),('B',90),('c',80)]
# student.sort(key=lambda s:s[1])
# print(student)
# for j in range(0,-1,-1):
#     print(j)
#InsertionSort
@decorator
def insertion_sort(name, arr):
    for i in range(1,len(arr)):
        index = i
        for j in range(i-1,-1,-1):
            if(arr[j]>arr[index]):
                arr = swap(arr,index,j)
                index -= 1
            else: break
    #     print(arr)
    # print(arr)
# name = 'insertion sort'
# print(a)
# insertion_sort(name,a)
@decorator
def insertion_sort_optimal(name, arr):
    for i in range(1, len(arr)):
        i_value = arr[i]
        loc = 0
        for j in range(i-1, -1, -1):
            if(i_value < arr[j]):
                arr[j+1] = arr[j]
            else:
                loc = j+1
                break
        arr[loc] =  i_value
#         print(arr)
#     print(arr)

# name = 'insertion sort optimal'
# print(a)
# insertion_sort_optimal(name,a)
@decorator
def bubble_sort(name, arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if(arr[j] > arr[j+1]):
                arr = swap(arr,j,j+1)
#     print(arr)
# name = 'bubble sort'
# print(a)
# bubble_sort(name,a)

@decorator
def shell_sort(name, arr):
    n = len(arr)
    d = n // 2
    while(d>0):
        for i in range(d,n):
            i_value = arr[i]
            j = i
            while(j>=d and arr[j-d]>i_value):
                arr[j] = arr[j-d]
                j -= d
            arr[j] = i_value
        d = d // 2
#     print(arr)
# name = 'shell sort'
# print(a)
# shell_sort(name,a)


        

      
