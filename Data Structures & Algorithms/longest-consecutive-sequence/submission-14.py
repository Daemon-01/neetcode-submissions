class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set()
        maxStreak = 0
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if num - 1 not in numSet:
                curStreak, j = 1, 0
                while (num + 1) in numSet and j < len(numSet):
                    curStreak, j = curStreak + 1, 0
                    num = num + 1
                if maxStreak < curStreak:
                    maxStreak = curStreak
        return maxStreak
