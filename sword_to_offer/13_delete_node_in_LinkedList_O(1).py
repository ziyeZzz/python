# -*- coding: utf-8 -*-
# 此题主要是 在O(1)时间删除链表结点。将当前要删结点复制为后一个结点，再删后一个结点。
'''
Q: 在O(1)时间删除链表结点
给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。
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
    def add_node(self, dataOrNode):
        if not isinstance(dataOrNode, Node):
            dataOrNode = Node(dataOrNode)

        if self.length == 0:
            self.head = dataOrNode
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = dataOrNode

    # O(1)思路: 将要删结点复制成其后一个结点，再删掉其后一个结点
    # 当前结点前一个结点不通过遍历不知道其信息，但当前要删结点的后一个结点是清楚的
    # 将当前要删结点的后一个结点的data复制给当前结点，再将当前._next改成后一个结点的._next
    def delete_in_O1(self, i):
        # 无效指针
        if i<0 or i>=self.length:
            return 'invalid delete index'
        # 空链表
        elif self.length == 0:
            return 'empty linked list'
        # 删除头结点
        elif self.length == 1:
            self.head = None
            self.length = 0
        # 删除尾结点，因为尾结点没有后一个结点的data可以复制给当前结点，故需要用原始方法从头到尾遍历一遍找到该需要删除的结点
        elif i == self.length-1:
            node = self.head
            j = 0
            while j < i:
                node = node._next
                j += 1
            node._next = None
        else:
            # 由于此题涉及到指针，暂不实现具体代码，思路可以借鉴
            # 当
            return None

