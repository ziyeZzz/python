# -*- coding:utf-8 -*-
'''
Q: 反转链表
定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self._next = None
    def __repr__(self):
        return str(self.data)

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

    # 思路：就像栈一样，倒出来。将每次读到的新node的_next设为当前链表的head，
    def reverse(self):
        if self.length == 0:
            return 'Empty linked list'
        node = self.head
        rev_head_node = Node(self.head.data)
        while node._next:
            new_head_node = Node(node._next.data)
            new_head_node._next = rev_head_node
            rev_head_node = new_head_node
            node = node._next
        self.head = rev_head_node

    def __repr__(self):
        if self.length == 0:
            return 'Empty linked list'
        node = self.head
        list =''
        while node:
            list += str(node.data) + ' '
            node = node._next
        return list

if __name__ == '__main__':
    my_linked_list = linked_list()
    for i in range(1, 11):
        my_linked_list.append(i)
    print(my_linked_list.__repr__())
    my_linked_list.reverse()
    print(my_linked_list.__repr__())


