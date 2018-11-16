#快速排序 O(nlogn)
a = [3,2,4,1,5,7,3]
#quick sort 3 ways: [<],[=],[>]
def quick_sort(arr):
    smaller = []
    bigger = []
    equal = []
    if(len(arr)>1):
        pivot = arr[0]
        for i in arr:
            if i > pivot:
                bigger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                equal.append(i)
        return quick_sort(smaller)+equal+quick_sort(bigger)
    else:
        return arr

print(quick_sort(a))

