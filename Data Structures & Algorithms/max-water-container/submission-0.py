class Solution:
    def maxArea(self, A: List[int]) -> int:
        maxArea = 0
        l,r = 0,len(A)-1
        while(l<r):
            curArea = (r-l) * min(A[l],A[r])
            maxArea = max(maxArea,curArea)
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return maxArea