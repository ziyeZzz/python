#binary search can only work on sorted array
def my_binary_search(arr,v):
    first = 0
    last = len(arr)-1
    found = False
    mid_index = 0
    while first<=last and not found:
        # mid_index = (first+last) // 2 -> when the number is very big, this method may cause memory overflow
        mid_index = first + (last-first)//2
        if(arr[mid_index]==v):
            found = True
        else:
            if(arr[mid_index]>v):
                last = mid_index - 1
            else:
                first = mid_index + 1
    #find lower and higher bound for duplicate values
    if(found):
        lower_bound = mid_index
        first_l = mid_index-1#first last
        while first<=first_l:
            mid = first + (first_l-first)//2
            if(arr[mid]==v):
                lower_bound = mid
                first_l = mid-1
            else:
               first = mid + 1
        higher_bound = mid_index
        last_s = mid_index+1#last start
        while last_s<=last:
            mid = last_s + (last-last_s)//2
            if(arr[mid]==v):
                higher_bound = mid
                last_s = mid+1
            else:
                last = mid -1
        return arr[lower_bound:higher_bound+1]
    else: return []


if __name__ == '__main__':
    a = [1,2,2,3,4,4,4,5,5,6]
    i = 2
    print(my_binary_search(a,i))