# -*- coding:utf-8 -*-
# 此题主要是 考察不合法输入是否会导致代码崩溃。鲁棒性
'''
Q: 链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。本题从1开始计数，即链表的尾结点是倒数第一个结点。
如链表共6个结点，从头结点开始它们的值依次是1、2、3、4、5、6，此链表倒数第3个结点是值为4的结点。

注：类似的问题还有，
返回链表中间结点：两个指针同时从头结点出发，p1一次走1步，p2一次2步。p2到尾时，p1正好在链表中间
判断单向链表是否形成了环形：两个指针同时从头结点出发，p1一次1步，p2一次两步。如果p2追上了p1，则是环。如果p2走到链表末尾还没追上p1，则不是环

总结：当一个指针遍历链表不能解决问题时，尝试两个指针来遍历链表。可以让其中一个指针遍历的速度快一些，或者让它先在链表上走若干步。
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self._next = None
    def __repr__(self):
        return self.data

class linked_list(object):
    def __init__(self):
        self.head = None
        self.length = 0
    def append(self, dataOrNode):
        if not isinstance(dataOrNode, Node):
            dataOrNode = Node(dataOrNode)
        if self.length == 0:
            self.head = dataOrNode
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = dataOrNode
            self.length += 1

    # 要考虑到if、elif中的问题输入。保证代码的鲁棒性
    def print_kth_from_end(self, k):
        if self.length == 0:
            return 'Empty linked list'
        elif self.length < k or k < 1:
            return 'Invalid k'
        else:
            k_from_head = self.length - k
            node = self.head
            count = 0
            while count < k_from_head:
                node = node._next
                count += 1
            return str(node.data)

    #假如不知道链表的长度，可以用两个指针p1,p2，间隔k。当p2移到链表尾部时，p1指向的就是要输出的node
    def print_kth_from_end2(self,k):
        if self.length == 0:
            return 'Empty linked list'
        elif self.length < k or k < 1:
            return 'Invalid k'
        else:
            node_1, node_2 = self.head,self.head
            for i in range(0,k-1):
                node_2 = node_2._next
            while node_2._next:
                node_2 = node_2._next
                node_1 = node_1._next
            return str(node_1.data)

if __name__ == '__main__':
    list = linked_list()
    for i in range(1,7):
        list.append(i)
        print(str(i)+' ',end="")
    print('\n')
    print(list.print_kth_from_end(3))
    print(list.print_kth_from_end2(3))


