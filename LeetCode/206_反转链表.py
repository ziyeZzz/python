'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

迭代 和 递归
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
# 迭代
def reverseList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre
# 递归
def reverList2(head):
    if head == None or head.next == None:
        return head
    p = reverList2(head.next)
    head.next.next=head
    head.next=None
    return p
