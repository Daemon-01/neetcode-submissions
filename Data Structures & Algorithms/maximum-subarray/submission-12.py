class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = res = nums[0]
        for i in range(1 , len(nums)):
            sum = max(sum + nums[i] , nums[i])
            res = max(res, sum)
        return res
