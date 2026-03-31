# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if curr == None:
            return False
        count = 0
        
        while count <= 1000:
            if curr.next == None:
                return False 
            curr = curr.next
            count += 1
        
        return True
        

