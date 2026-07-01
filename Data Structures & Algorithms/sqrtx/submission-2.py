class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l<=r:
            mid = l + (r-l) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                l = mid + 1
            else:
                r = mid - 1
        return r