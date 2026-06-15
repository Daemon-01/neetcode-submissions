class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        result = []
        for i in range(0,len(A)):
            if i>0 and A[i] == A[i-1]:
                continue
            k = len(A)-1
            j = i+1
            while(j<k):
                if(A[i]+A[j]+A[k] == 0):
                    result.append([A[i],A[j],A[k]])
                    while(j<k and A[j]==A[j+1]):
                        j += 1
                    while(j<k and A[k]==A[k-1]):
                        k -= 1
                    j,k = j+1,k-1
                elif(A[i]+A[j]+A[k] > 0):
                    k -= 1
                else:
                    j += 1
        return result
                           
