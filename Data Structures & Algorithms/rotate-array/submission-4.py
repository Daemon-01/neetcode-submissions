class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(A)-1
        while(l<r):
            A[l],A[r] = A[r],A[l]
            l,r = l+1,r-1
        if k >= len(A):
            k = k%len(A)
        l,r = 0,k-1
        while(l<r):
            A[l],A[r] = A[r],A[l]
            l,r = l+1,r-1
        l,r = k,len(A)-1
        while(l<r):
            A[l],A[r] = A[r],A[l]
            l,r = l+1,r-1