class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        caching = {}

        def dfs(idx1, idx2, cur_str):
            key = (idx1, idx2)
            if key in caching:
                return caching[key]
            if len(cur_str) == len(t):
                return 1
            if idx1 == len(s):
                return 0
            
            count = 0

            count += dfs(idx1 + 1, idx2 + 1, cur_str + t[idx2]) if s[idx1] == t[idx2] else 0
            count += dfs(idx1 + 1, idx2, cur_str)
            caching[key] = count
            return count
        
        return dfs(0, 0, "")