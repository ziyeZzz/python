#-*- coding: utf-8 -*-
# 此题主要是右上，左下指针移动。每次判断完要么移右上要么移左下
'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序
      每一行都按照从上到下递增的顺序排序。请完成一个函数，
      输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
这个代码是用二维数组最右上角的数与要找的数对比，再来移动行或列
同理，也可以从左下角。对矩阵n*n，此算法复杂度为O（n）。
注： 从左上角或右下角分析则不好。因其无法彻底排除某一行或一列。没有利用好这个递增二维数组的特性
'''
import numpy as np
def print2DArray(arr):
    print('Find a number in following array:')
    # for i in arr:
    #     print(i)
    print(arr)

#迭代思路，调用函数自己
def findNumIn2DArray(arr, num, flag):
    if flag==True:
        print('I found it!')
    elif arr is None:
        print('Not found. QAQ')
    else:
        arr_len = len(arr[0])#矩阵宽
        right_corner = arr[0, arr_len-1]
        if num < right_corner:
            if len(arr[0]) > 1:
                arr = arr[:,:arr_len-1]
            else:
                arr = None
        elif num > right_corner:
            if len(arr) > 1:
                arr = arr[1:,:]
            else:
                arr = None
        else:
            flag = True
        findNumIn2DArray(arr, num, flag)
    return flag

#指针移动，不迭代函数
def findNumIn2DArray_2(arr, num, flag):
    i = 0 #行数
    j = len(arr[0])-1 #列数
    while flag==False and i<len(arr) and j>=0:
        right_corner = arr[i,j]
        if right_corner > num:
            j = j - 1
        elif right_corner < num:
            i = i + 1
        else: flag = True
    if flag == True:
        print("I found it!")
    else:
        print("Not found. QAQ")


if __name__ == '__main__':
    #define two-dimensional array
    dyadic_array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    arr = np.array(dyadic_array)
    print2DArray(arr)
    # input num
    num = int(input('please enter a number:'))
    while num > 0:
        # find num in 2D-array
        #findNumIn2DArray(arr, num, False)
        findNumIn2DArray_2(arr, num, False)
        print2DArray(arr)
        # input num
        num = int(input('please enter a number:'))
