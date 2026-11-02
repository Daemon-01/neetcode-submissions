class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        cache = {0}
        
        for stone in stones:
            cache |= {s + stone for s in cache if s + stone <= target}
        
        best = max(cache)
        return sum(stones) - 2 * best