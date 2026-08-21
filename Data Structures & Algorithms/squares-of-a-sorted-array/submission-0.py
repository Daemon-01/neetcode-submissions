class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        res = [0] * n
        pos = n-1

        while l<=r:
            if (abs(nums[l]) > abs(nums[r])):
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1
        return res
            