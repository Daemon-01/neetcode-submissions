class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, best_max = 0, float("-inf")

        for num in nums:
            cur_max = max(num, cur_max + num)
            best_max = max(best_max, cur_max)
        
        return best_max