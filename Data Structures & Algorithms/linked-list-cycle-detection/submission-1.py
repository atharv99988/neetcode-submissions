# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head :
            return False
            
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer and fast_pointer : 
            if slow_pointer.next == fast_pointer.next and slow_pointer.val == fast_pointer.val :
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = None if not fast_pointer.next else fast_pointer.next.next

        return False
        
        