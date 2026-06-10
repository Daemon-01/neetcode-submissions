class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k , j = 0 , 0
        for num in nums:
            if num != val:
                k += 1
            else:
                r = j
                while(r < len(nums) and nums[r] == val):
                    r += 1
                if r < len(nums):
                    nums[j] , nums[r] = nums[r] , nums[j]
                    k += 1
            j += 1
        return k