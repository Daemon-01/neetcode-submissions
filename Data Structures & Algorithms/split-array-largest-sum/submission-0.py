class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1

        l,r = max(nums), sum(nums)

        while l<=r:
            mid = l + (r-l) // 2

            if self.subArrayCount(nums,mid) <= k:
                r = mid - 1
            else:
                l = mid + 1
        return l

    
    def subArrayCount(self,nums,maxSum) -> int:
        curSum = 0
        subCount = 1

        for num in nums:
            if curSum + num <= maxSum:
                curSum += num
            else:
                subCount += 1
                curSum = num
        return subCount