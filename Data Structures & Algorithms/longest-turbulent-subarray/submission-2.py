class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        cur_max = cur_reverse = best_max = 1

        for i in range(len(nums) - 1):
            if i % 2 == 0:
                cur_max = cur_max + 1 if nums[i] < nums[i + 1] else 1
                cur_reverse = cur_reverse + 1 if nums[i] > nums[i + 1] else 1
            else:
                cur_max = cur_max + 1 if nums[i] > nums[i + 1] else 1
                cur_reverse = cur_reverse + 1 if nums[i] < nums[i + 1] else 1

            best_max = max(best_max, cur_max, cur_reverse)

        return best_max