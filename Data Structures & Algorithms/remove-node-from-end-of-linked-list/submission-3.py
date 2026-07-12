# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        # detecing the last node before the one that needs to be removed
        last = N - n
        cur = head
        prev = None
        for _ in range(1,last+1):
            prev = cur
            cur = cur.next
        
        # remoing the desired node
        if cur == head:
            head = head.next
            cur.next = prev
        else:
            prev.next = cur.next
            cur.next = None
        return head