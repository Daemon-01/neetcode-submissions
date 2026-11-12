class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        caching = {}

        def dfs(i, j):
            key = (i, j)
            if key in caching:
                return caching[key]
            
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            
            if word1[i] == word2[j]:
                res = dfs(i-1, j-1)
            else:
                insert = dfs(i, j-1)
                delete = dfs(i-1, j)
                replace = dfs(i-1, j-1)
                res = min(insert, delete, replace) + 1
            
            caching[key] = res
            return res
        return dfs(len(word1)-1, len(word2)-1)