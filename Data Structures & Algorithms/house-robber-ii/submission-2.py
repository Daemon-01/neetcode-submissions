class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        skip_first = [0] * (n+1)
        skip_first[0], skip_first[1] = 0, 0
        skip_last = [0] * (n)
        skip_last[0], skip_last[1] = 0, nums[0]

        for i in range(2,n):
            skip = skip_last[i-1]
            rob = skip_last[i-2] + nums[i-1]

            skip_last[i] = max(rob, skip)
        
        for i in range(2, n+1):
            skip = skip_first[i-1]
            rob = skip_first[i-2] + nums[i-1]

            skip_first[i] = max(rob, skip)
        
        return max(skip_first[n], skip_last[n-1])