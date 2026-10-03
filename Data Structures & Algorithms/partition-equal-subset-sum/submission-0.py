class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        possible = {0}
        for num in nums:
            new_sums = set()
            for cur in possible:
                new_sums.add(num+cur)
            possible |= new_sums

            if target in possible:
                return True
        return target in possible
