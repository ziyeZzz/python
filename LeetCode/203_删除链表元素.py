# encoding:utf-8
'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, val):
    tmp = ListNode(0)
    tmp.next = head
    node = tmp
    while node.next:
        if node.next.val == val:
            node.next = node.next.next
        else: node = node.next
    head = tmp.next
    return head
            