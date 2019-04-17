'''
编写一个程序，找到两个单链表相交的起始节点。
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def getIntersectionNode(headA,headB):
    return 0