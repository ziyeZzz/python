#-*- coding: utf-8 -*-
'''
Q：请实现一个函数，把字符串中的每个空格替换成“%20”。
    例如输入“We are happy”，则输出“We%20ar%20happy”

注：本题使用python解决固然简单，但当用C/C++语言解决时，其背后思想值得借鉴
    需注意，将空格替换成“%20”后，每次替换会增加两个字节的存储空间。
    分两种情况：
        1）新建字符串：
            此种情况可以保证足够多的内存，可以从前往后复制。其复杂度为O（n）;
        2) 在原字符串上操作：
            如果从前往后，将原空格替换成“%20”，会导致后面的字符串不断被移动。
            假设字符串长度是n，对每个空格字符，需移动后面O（n）个字符，
            因此对含O（n）个空格字符的字符串而言，其总时间效率是O（n^2）
            但转变思路，
            先遍历一遍字符串，算出总所需长度后，从后往前复制。则不需要再移动任何字符串了，
            直接覆盖就行了。此时时间复杂度为O（n）
'''
def replace_blankSpace(str, replace_to):
    replaced_str = str.replace(' ',replace_to)
    return replaced_str


if __name__ == '__main__':
    str = input('Please input a string:')
    replace_to = "%20"
    replaced_str = replace_blankSpace(str, replace_to)
    print(replaced_str)