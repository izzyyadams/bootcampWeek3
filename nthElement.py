# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        target = head
        current = head
        previous = None
        for i in range(n):
            target=target.next
        if not target:
            return head.next
        while target:
            previous = current
            current = current.next
            target = target.next
        previous.next = current.next
        return head
