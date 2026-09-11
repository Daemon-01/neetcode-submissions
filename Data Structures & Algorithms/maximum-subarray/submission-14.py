class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]

        l = 0
        sum = 0
        res = float("-inf")
        for i in range(len(nums)):
            while l < i and sum <= 0:
                sum -= nums[l]
                l += 1
            sum += nums[i]
            res = max(res, sum)
        return res
