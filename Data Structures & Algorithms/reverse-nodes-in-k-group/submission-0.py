# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt, cur = 0, head
        while cur:
            cnt += 1
            cur = cur.next
        
        cur = head
        first, last = None, None

        for i in range(1, cnt+1 , k):
            if i+k-1 <= cnt:
                last = self.reverse(cur, k)
                if first:
                    first.next = last
                else:
                    head = last
                first = cur
                cur = cur.next
            else:
                if first:
                    first.next = cur
                break
        return head

    def reverse(self, node, k):
        prev = None
        cur = node
        while k > 0 and cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            k -= 1
        node.next = cur
        return prev
         