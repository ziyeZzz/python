#归并排序 O(nlogn)
def merge_sort(arr):
    def merge(left, right):
        i = j = 0
        arr_merge = []
        while(i < len(left) and j <len(right)):
            if(left[i]<right[j]):
                arr_merge.append(left[i])
                i += 1
            else:
                arr_merge.append(right[j])
                j += 1
        if(i>=len(left) and j<len(right)):
            for a in right[j:]:
                arr_merge.append(a)
        elif(j>=len(right) and i<len(left)):
            for a in left[i:]:
                arr_merge.append(a)
        return arr_merge

    if(len(arr)>1):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        arr = merge(left, right)
    return arr

# print(a)
# print(merge_sort(a))
    
i = [2,3,1]
print(sorted(i))
i.sort()
print(i)