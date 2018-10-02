# -*- coding:utf-8 -*-
'''
Q: 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
如：L1-> 1 3 5 7, L2-> 2 4 6 8, 合并后 L3-> 1 2 3 4 5 6 7 8
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

    def __repr__(self):
        if self.length == 0:
            return 'Empty linked list'
        node = self.head
        list = ''
        while node:
            list += str(node.data) + ' '
            node = node._next
        return list

def merge(l1, l2):
    # 检查输入是否合理。代码鲁棒性~~♪(^∇^*)
    if l1.length == 0 and l2.length == 0:
        return 'two empty linked list'
    elif l1.length == 0:
        return l2
    elif l2.length == 0:
        return l1
    else:
        node_1 = l1.head
        node_2 = l2.head
        list = linked_list()
        # 两个指针，比较两个链表所指元素大小。小的先加入新链表。
        while node_1 and node_2:
            if node_1.data < node_2.data:
                list.append(Node(node_1.data))
                node_1 = node_1._next
            else:
                list.append(Node(node_2.data))
                node_2 = node_2._next
        # 两个链表长度可能不一样，需判断是否还有剩余未加node。注意：不需要用while一个个加。因为链表node自动已经带了._next。所以只用加一次就够了。
        if node_1:
            list.append(node_1)
        if node_2:
            list.append(node_2)
    return list

if __name__ == '__main__':
    l1 = linked_list()
    l2 = linked_list()
    for i in range(1,15,2):
        l1.append(i)
    for i in range(2,9,2):
        l2.append(i)
    l3 = merge(l1, l2)
    print(l3.__repr__())


