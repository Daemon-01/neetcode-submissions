# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Phase 1: Find the peak index using binary search
        l, r = 0, n - 1
        peak = 0
        while l < r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # Phase 2: Binary search on the ascending (left) slope
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        # Phase 3: Binary search on the descending (right) slope
        l, r = peak + 1, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:  # Note: opposite logic because the array is decreasing
                l = mid + 1
            else:
                r = mid - 1

        return -1