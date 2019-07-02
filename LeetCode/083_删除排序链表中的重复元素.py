'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
'''
class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

# 循环
def deleteDuplicates(head):
    node = head
    while node and node.next:
        if node.val==node.next.val:
            node.next = node.next.next
        else:node = node.next
    return head

# 网友写的递归
def deleteDuplicates2(head):
    if head==None or head.next==None:
        return head
    head.next = deleteDuplicates2(head.next)
    if(head.val == head.next.val):
        head=head.next
    return head

a = ListNode(1)
a.next=ListNode(1)
a.next.next=ListNode(2)
a.next.next.next=ListNode(3)
a.next.next.next.next=ListNode(3)
print(deleteDuplicates(a))

