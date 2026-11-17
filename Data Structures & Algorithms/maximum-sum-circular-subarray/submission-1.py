class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min = 0, 0
        best_max, best_min = float("-inf"), float("inf")
        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            best_max = max(best_max, cur_max)
            cur_min = min(cur_min + num, num)
            best_min = min(cur_min, best_min)
            total += num
        
        if best_max < 0:
            return best_max
        
        return max(best_max, total - best_min)