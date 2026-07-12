# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Count the exact number of nodes (N)
        cur = head
        N = 1
        while cur:
            cur = cur.next
            N += 1
        
        # 2. Perform exactly (N - 1) // 2 swaps
        cur = head
        total_swaps = (N - 1) // 2
        for _ in range(total_swaps):
            self.swaps(head, cur)
            cur = cur.next.next  # Safely jump over the inserted node
        
    def swaps(self, head, cur) -> None:
        tail = head
        # Find the node right before the last node (the second-to-last node)
        while tail.next and tail.next.next:
            tail = tail.next
        
        # Move the last node (tail.next) right after 'cur'
        tmp = tail.next
        tail.next = None  # Sever the last node from the end
        tmp.next = cur.next
        cur.next = tmp