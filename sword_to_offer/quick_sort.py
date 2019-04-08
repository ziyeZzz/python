# def quickSort(L):
#     return q_sort(L,0,len(L)-1)
#
# def q_sort(L,left,right):
#     if left<right:
#         pivot=Partition(L,left,right)
#
#         q_sort(L,left,pivot-1)
#         q_sort(L,pivot+1,right)
#     return L
#
# def Partition(L,left,right):
#     pivotkey=L[left]
#     while left<right:
#         while left<right and L[right]>=pivotkey:
#             right-=1
#         L[left]=L[right]
#         while left<right and L[left]<=pivotkey:
#             left+=1
#         L[right]=L[left]
#
#     L[left]=pivotkey
#     return left



def partition(L,left,right):
    pivot_key=L[left]
    while left<right:
        while left<right and L[right]>=pivot_key:
            right -= 1
        L[left]=L[right]
        while left<right and L[left]<=pivot_key:
            left += 1
        L[right]=L[left]
    L[left]=pivot_key
    return left

def q_sort(L,left,right):
    if left<right:
        pivot=partition(L,left,right)
        q_sort(L,left,pivot-1)
        q_sort(L,pivot+1,right)
    return L

def quick_sort(L):
    return q_sort(L,0,len(L)-1)

L=[5,9,1,11,6,7,2,4]
#print(quickSort(L))
print(quick_sort(L))