class Solution:
    def numRescueBoats(self, A: List[int], limit: int) -> int:
        l,r=0,len(A)-1
        A.sort()
        boats = 0
        while(l<=r):
            if l != r and A[l]+A[r] <= limit:
                l,r = l+1,r-1
                boats += 1
            elif l==r:
                boats += 1
                l,r = l+1,r-1
            else:
                r -= 1
                boats += 1
        return boats
            