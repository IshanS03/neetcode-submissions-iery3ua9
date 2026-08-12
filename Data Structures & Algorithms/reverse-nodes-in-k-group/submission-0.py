# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        node = head
        length = 0

        while node:
            length += 1
            node = node.next

        headTemp = head
        cycles = length // k
        if cycles == 0:                 
            return head
        last = None
        for i in range(cycles):
            node = headTemp
            dummy = None                
            size = k

            while size:
                nextNode = node.next
                node.next = dummy
                dummy = node
                node = nextNode
                size -= 1

            if i == 0:
                res = dummy

            if last:                   
                last.next = dummy
            last = headTemp            
            headTemp = node             

        last.next = headTemp           
        return res


            

        
            

        