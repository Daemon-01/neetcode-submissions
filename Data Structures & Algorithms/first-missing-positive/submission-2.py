class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        myset = set()
        for num in nums:
            if num>=0:
                myset.add(num)
        if len(myset) == 0:
            return 1
        largest = max(myset)
        for i in range(0,largest+1):
            if (i+1) not in myset:
                return i+1