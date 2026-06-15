class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l,r=0,1
        k = 1
        for i in range(1,len(nums)):
            if nums[l] == nums[i]:
                continue
            else:
                tmp = nums[l+1]
                nums[l+1] = nums[i]
                nums[i] = tmp
                l,k = l+1,k+1
        return k