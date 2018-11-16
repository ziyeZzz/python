#get the n-th[0,len(arr)) biigest number in a list. O(n)
#use the same idea as quick sort
import random
a = [4,2,6,3,4,6,1]
def the_n_num(arr, n):
    if(len(arr)>1):
        i = random.randint(0,(len(arr)-1))
        pivot = arr[i]
        # print('i:'+str(i)+', pivot:'+str(pivot))
        smaller = []
        bigger = []
        equal = []
        for m in arr:
            if m>pivot:
                bigger.append(m)
            elif m<pivot:
                smaller.append(m)
            else:
                equal.append(m)
        # print('smaller:',smaller,'equal:',equal,'bigger:',bigger)
        if(n<len(smaller)):
            return the_n_num(smaller, n)
        elif n>=(len(smaller)+len(equal)):
            return the_n_num(bigger,n-(len(smaller)+len(equal)))
        else:
            return equal
    else:
        return arr

n = 0
print(a,sorted(a))
print('n:',n,', the number is:',the_n_num(a, n)[0])

