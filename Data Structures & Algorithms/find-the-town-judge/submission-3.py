class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        townJudge = [0] * (n+1)

        for ai, bi in trust:
            townJudge[ai] -= 1
            townJudge[bi] += 1
        
        for i, num in enumerate(townJudge):
            if num == (n-1):
                return i
        return -1