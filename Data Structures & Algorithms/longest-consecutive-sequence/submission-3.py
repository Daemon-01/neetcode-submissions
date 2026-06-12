class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set()
        maxStreak = 1
        for num in nums:
            numSet.add(num)
        for num in nums:
            if (num+1) in numSet:
                curStreak , j = 1 , 0
                while(num+1 in numSet and j < len(numSet)):
                    curStreak += 1
                    num = num+1
                if maxStreak < curStreak:
                    maxStreak = curStreak
        return maxStreak
