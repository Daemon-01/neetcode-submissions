class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqCount = {}
        result = []
        for num in nums:
            freqCount[num] = freqCount.setdefault(num,0) + 1
        for key , val in freqCount.items():
            if val > len(nums)//3:
                result.append(key)
        return result