class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left , right = 0, len(nums) -1
        hash_map = {}

        for i, num in enumerate(nums):
            find = target - num
            if find in hash_map:
                return [min(hash_map[find], i), max(hash_map[find], i)]
            hash_map[num] = i