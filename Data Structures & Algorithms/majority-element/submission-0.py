class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCount = {}
        for num in nums:
            freqCount[num] = freqCount.setdefault(num,0) + 1
            if freqCount[num] > len(nums)/2:
                return num