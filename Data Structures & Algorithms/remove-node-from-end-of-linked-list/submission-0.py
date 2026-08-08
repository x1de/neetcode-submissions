# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        target_index = length - n
        curr_index = 0
        prev = ListNode(None)
        temp = prev
        curr = head
        while curr:
            if target_index == curr_index:
                prev.next = curr.next
                curr = None
            else:
                prev.next = curr
                curr = curr.next
                prev = prev.next
                curr_index+=1
        return temp.next