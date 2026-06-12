class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        setNum = set()
        maxStreak = 1
        for num in nums:
            setNum.add(num)
        for num in nums:
            curStreak = 1
            j = 0
            while(num-1 in nums and j < len(nums)):
                curStreak += 1
                j += 1
                num = num-1
            if curStreak > maxStreak:
                maxStreak = curStreak
        return maxStreak
