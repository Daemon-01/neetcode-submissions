class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = []
        for i in range(len(nums)):
            j = i-1
            leftProd = 1
# product of the left side number
            while(j>=0):
                leftProd *= nums[j]
                j -= 1
            left.append(leftProd)
# product of the right side of the number
            j = i+1
            rightProd = 1
            while(j<len(nums)):
                rightProd *= nums[j]
                j += 1
            right.append(rightProd)
# final multiplication of the 2 arrays
        for i in range(len(nums)):
            result.append(right[i]*left[i])
        return result
        
