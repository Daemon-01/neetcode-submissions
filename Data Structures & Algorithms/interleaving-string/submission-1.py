class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def combine(idx1, idx2):
            key = (idx1, idx2)
            k = idx1 + idx2

            if key in memo:
                return memo[key]

            if k == len(s3):
                return True

            res = False

            if idx1 < len(s1) and s1[idx1] == s3[k]:
                res = combine(idx1 + 1, idx2)
            
            if not res and idx2 < len(s2) and s2[idx2] == s3[k]:
                res = combine(idx1, idx2 + 1)
            
            memo[key] = res
            return res
        
        return combine(0, 0)