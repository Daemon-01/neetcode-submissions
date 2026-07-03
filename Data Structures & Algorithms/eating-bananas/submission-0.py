import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                res = mid
                right = mid - 1  # try smaller rate
            else:
                left = mid + 1   # need faster rate

        return res
