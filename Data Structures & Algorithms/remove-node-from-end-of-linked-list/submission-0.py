# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go through the nodes and count how many there are 
        # loop until the count - nth node, and point that node to null, and the previous one to the next one
        count = 0
        root = head

        if not head:
            return
        
        while(head.next):
            count += 1
            head = head.next
        
        head = root
        count += 1
        
        # removing the first node
        if count == n:
            return head.next

        prev = None

        for _ in range(count - n):
            prev = head
            head = head.next

        prev.next = head.next
        return root
