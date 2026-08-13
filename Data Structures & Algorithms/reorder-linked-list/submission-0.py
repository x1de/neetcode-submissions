# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split the list into two
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        second = slow.next # Head of the second half
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge the two lists
        first_h, second_h = head, prev
        while second_h:
            tmp1 , tmp2= first_h.next, second_h.next
            first_h.next = second_h
            second_h.next = tmp1
            first_h = tmp1
            second_h = tmp2