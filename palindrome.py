# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fpointer = head
        spointer = head
        while fpointer and fpointer.next:
            spointer=spointer.next
            fpointer=fpointer.next.next
        
        previous = None
        current = spointer

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        firstHalf = head
        secondHalf = previous
        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            else:
                firstHalf = firstHalf.next
                secondHalf = secondHalf.next
        return True
