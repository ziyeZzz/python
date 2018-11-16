from max_heap import max_heap

def heap_sort(arr):
    mh = max_heap()
    for i in arr:
        mh.insert(i)
    mh.output_myheap()
    for i in range(len(arr)-1,-1,-1):
        arr[i] = mh.delete()
    # for i in range(0,len(arr)):
    #     arr[i] = mh.delete()
    print(arr)



if __name__ == '__main__':
    a = [3,2,1,5,4,8,7]
    heap_sort1(a)