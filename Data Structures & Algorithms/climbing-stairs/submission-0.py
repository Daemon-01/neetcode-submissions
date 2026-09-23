class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, next = 1, 2
        for i in range(3, n+1):
            cur = prev + next
            prev = next
            next = cur
        return next
