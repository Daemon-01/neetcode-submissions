class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return nums
        res = []
        l, largest = 0, float("-inf")

        for r in range(len(nums)):
            if largest < nums[r]:
                maxIdx = r
                largest = nums[r]
            if r-l+1 == k:
                res.append(largest)
                l += 1
                if(r+1<len(nums) and largest <= nums[r+1]):
                    largest = nums[r+1]
                else:
                    largest = float("-inf")
                    for i in range(l,l+k):
                        if i < len(nums):
                            largest = max(largest,nums[i])
        return res