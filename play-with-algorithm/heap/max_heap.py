#the implementation of max heap by using array
#1) insert n elements to an empty heap one by one, O(nlogn)
#2) heapify: shift down from i=count/2(the first not-leave node),i>=1,i--, O(n)
import random

class max_heap:
    def __init__(self):
        self.arr = [0]
        self.count = 0
    

    def swap(self,i,j):
        var = self.arr[j]
        self.arr[j] = self.arr[i]
        self.arr[i] = var

    def __shift_up(self,i):
        while(i>1 and self.arr[i//2]<self.arr[i]):
            self.swap(i,i//2)
            i = i//2
    
    def __shift_down(self,i):
        #while has left child
        while(i*2<=self.count):
            #left child index
            j = i*2
            #if has right child
            if(j+1 < self.count):
                #compare the values between left child and right child
                if(self.arr[j]<self.arr[j+1]):
                    j += 1
            #if parent value smaller than child bigger value
            if(self.arr[i]<self.arr[j]):
                self.swap(i,j)
                i = j
            else:
                break

    def insert(self,v):
        self.arr.append(v)
        self.count += 1
        self.__shift_up(self.count)
    
    def delete(self):
        heap_top = self.arr[1]
        self.arr[1] = self.arr[self.count]
        self.arr = self.arr[:-1]
        self.count -= 1
        self.__shift_down(1)
        return heap_top

    def output_myheap(self):
        i = 1
        j = 2
        print(self.arr)
        while(j<len(self.arr)):
            print(self.arr[i:j])
            i = j
            j = j *2
        if(i<=len(self.arr)):
            print(self.arr[i:])

if __name__ == '__main__':
    mh = max_heap()
    data = [] 
    for i in range(0,20):
        data.append(random.randint(0,50))
    print('original array list:')
    print(data)
    for i in data:
        mh.insert(i)
    print('heap in binary tree format:')
    mh.output_myheap()

    print('insert a number:')
    mh.insert(30)
    mh.output_myheap()

    print('delete a number:')
    mh.delete()
    mh.output_myheap()
        
