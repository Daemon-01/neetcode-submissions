class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canidate = None
        count = 0
        for num in nums:
            if count == 0:
                count += 1
                canidate = num
            elif num == canidate:
                count += 1
            elif num != canidate:
                count -= 1
        count = 0
        for num in nums:
            if num == canidate:
                count += 1
        if count>(len(nums)//2):
            return canidate
