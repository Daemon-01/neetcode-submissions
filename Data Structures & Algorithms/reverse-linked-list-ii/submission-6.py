# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        start, last = head, None
        cur = head

        #finding the starting node
        before = None
        for _ in range(left-1):
            before = start
            start = start.next
        
        # finding the last node to reverse
        cur1 = head
        for _ in range(right):
            last = cur1
            cur1 = cur1.next
        
        last.next = None
        cur, next = start, start
        dummy = start
        prev = None
        while cur:
            next = next.next
            cur.next = prev
            prev = cur
            cur = next
        
        if left == 1:
            head.next = cur1
            return prev
        else:
            before.next = prev
            dummy.next = cur1
            return head