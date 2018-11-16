#逆序对 O(nlogn)
a = [6,5,4,3,2,1]
count = 0
def invertion(arr):
    if(len(arr) > 1):
        d = len(arr) // 2
        left = invertion(arr[0:d])
        right = invertion(arr[d:])
        arr = merge(left,right)
    return arr

def merge(left,right):
    global count
    i = j = 0
    merge_arr = []
    while( i<len(left) and j<len(right)):
        if( left[i]>right[j]):
            merge_arr.append(right[j])
            count += len(left)-i
            j += 1
        else:
            merge_arr.append(left(i))
            i += 1
    if(i>=len(left) and j<len(right)):
        for m in right[j:]:
            merge_arr.append(m)
    elif(i<len(left) and j>= len(right)):
        for m in left[i:]:
            merge_arr.append(m)
    return merge_arr

print(invertion(a))
print(count)

        