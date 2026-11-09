class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        caching = {}
        n = len(piles)

        def stones(i, M):
            key = (i, M)
            if i == n:
                return 0
            if key in caching:
                return caching[key]

            rem = sum(piles[i:])
            if n - i <= 2 * M:
                return rem
            
            best, max_take = 0, min(2*M, n - i)
            for x in range(1, max_take + 1):
                next_M = max(M, x)
                opponent_stones = stones(i+x, next_M)
                current_player_stones = rem - opponent_stones
                best = max(best, current_player_stones)
            caching[key] = best
            return best
        
        return stones(0, 1)