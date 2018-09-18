#-*- coding: utf-8 -*-
#新建链表，数据插入，删除，输出链表，反向输出链表
'''
Q: 输入一个链表的头结点，从尾到头反过来打印出每个结点的值

通常打印是一个只读操作，我们不希望打印时修改内容。最好先问面试官能否修改链表的结构，将其倒置后输出。
'''

#链表的结点
import sys
class Node(object):
    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)

#链表
class linkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data)+' '
            node = node._next
        return nlist

    #反转输出，倒序累加法，借用栈的思想
    def reverse_print(self):
        if self.isEmpty():
            return "the chain table is empty"
        nlist = ''
        node = self.head
        while node:
            nlist = str(node.data) + ' ' + nlist
            node = node._next
        return nlist

    # def reverse_print_2(self):
    #     if self.isEmpty():
    #         return "the chain table is empty"
    #     def print_node(node):
    #         while node:
    #             print(print_node(node._next)+' ')


    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("This chain table is empty.")
            return

        if index < 0 or index > self.length:
            print("Error: please input a valid index")
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    #在index前插入，index valid from 0 to length-1
    def insert(self, index, dataOrNode):
        if index < 0 or index >= self.length:
            print("Error: out of inserting boundary.")
            return

        if self.length == 0:
            print("This chain table is empty.")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev._next = item
            item._next = node
            self.length += 1

if __name__ == '__main__':
    my_linkedList = linkedList()
    while True:
        code = input('Give me command'+'\n'+
                     '(q:quit, p:print, rp:reversely print, a:append, i:insert, d:delete,):')
        if code == 'q':
            sys.exit()
        elif code == 'p':
            print(my_linkedList.__repr__())
        elif code == 'rp':
            print(my_linkedList.reverse_print())
        elif code =='a':
            append_content = input('please input append data:')
            my_linkedList.append(append_content)
        elif code =='i':
            try:
                index,data = input('please input insert index and data:').split()
                my_linkedList.insert(int(index),data)
            except ValueError:
                print("Error: please check your input")
        elif code == 'd':
            index = input('please input delete index:')
            my_linkedList.delete(int(index))
        else:
            print('please input valid command')
