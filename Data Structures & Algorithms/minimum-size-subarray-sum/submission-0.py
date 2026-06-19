class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l = 0
        res = sys.maxsize
        for r in range(len(nums)):
            sum += nums[r]
            while(l<=r and sum >= target):
                sum -= nums[l]
                res = min(res,r-l+1)
                l+=1
        return 0 if res == sys.maxsize else res