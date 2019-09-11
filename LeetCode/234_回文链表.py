'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(self, head):
    # find middle node
    left_head = None
    slow= head
    fast = head.next
    while fast.next:
        left_head = slow.next
        tmp = slow.next.next
        left_head.next = slow
        slow.next = tmp
        slow = slow.next
        fast = fast.next.next
    
    while slow and left_head:
        if slow.val != left_head.val:
            return False
        else:
            slow = slow.next
            left_head = left_head.val
    return False
    
