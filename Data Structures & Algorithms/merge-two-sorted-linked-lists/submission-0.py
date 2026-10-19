# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        head = newHead
        listA = list1
        listB = list2

        while listA and listB : 
            if listA.val <= listB.val : 
                newHead.next = listA
                newHead = newHead.next
                listA = listA.next
            else : 
                newHead.next = listB
                newHead = newHead.next
                listB = listB.next
        
        if listA : 
            newHead.next = listA
        
        if listB : 
            newHead.next = listB
        
        return head.next

        