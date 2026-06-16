class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        n = len(A)
        A.sort()
        result = []
        for i in range(len(A)):
            if i>0 and A[i] == A[i-1]:
                continue
            for j in range(i+1,len(A)):
                if j > i+1 and A[j] == A[j-1]:
                    continue
                l,r = j+1,len(A)-1
                while(l<r):
                    if(A[i]+A[j]+A[l]+A[r] == target):
                        result.append([A[i],A[j],A[l],A[r]])
                        while(l<r and A[l]==A[l+1]):
                            l += 1
                        while(l<r and A[r]==A[r-1]):
                            r -= 1
                        l,r = l+1,r-1
                    elif(A[i]+A[j]+A[l]+A[r] < target):
                        l += 1
                    else:
                        r -= 1
        return result