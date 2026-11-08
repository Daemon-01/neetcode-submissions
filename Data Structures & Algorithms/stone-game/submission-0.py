class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        caching = {} # stores the l, r indices for sub-array for Alice score

        def dfs(l, r):
            if l > r: # checks if we have run out of choices
                return 0
            if (l, r) in caching:
                return caching[(l, r)]
            
            even = True if (r-l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            caching[(l, r)] = max(dfs(l + 1, r) + left,
                                  dfs(l, r - 1) + right)
            return caching[(l ,r)]
        
        return dfs(0, len(piles) - 1) > sum(piles) // 2