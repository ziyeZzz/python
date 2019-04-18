'''
编写一个程序，找到两个单链表相交的起始节点。
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def getIntersectionNode(headA,headB):
    if headA == None or headB == None:
        return False
    pA = headA
    pB = headB
    while pA != pB:
        if pA != None:
            pA = pA.next
        else:
            pA = headB
        if pB != None:
            pB = pB.next
        else:
            pB = headA
    return pA