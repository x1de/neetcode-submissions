# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp1 = temp2 = head
        while head:
            length+=1
            head = head.next
        target = length - n
        if target == 0:
            return temp1.next

        index = 0
        while temp2:
            if index +1 == target:
                temp2.next = temp2.next.next
                break
            temp2 = temp2.next
            index+=1
        return temp1