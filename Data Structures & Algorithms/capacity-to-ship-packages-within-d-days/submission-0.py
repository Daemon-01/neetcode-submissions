class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        res = r

        while l<=r:
            mid = l + (r-l) // 2
            weight = 0
            days_needed = 1
            for w in weights:
                if weight + w > mid:
                    weight = 0
                    days_needed += 1
                weight += w
            if days_needed <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
