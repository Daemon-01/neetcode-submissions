from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Trust scores for persons 1 to n (index 0 is unused)
        trust_scores = [0] * (n + 1)
        
        # Calculate net trust scores
        for a, b in trust:
            trust_scores[a] -= 1  # Person 'a' trusts someone, decrease score
            trust_scores[b] += 1  # Person 'b' is trusted, increase score
            
        # Check if anyone meets the judge criteria
        for person in range(1, n + 1):
            if trust_scores[person] == n - 1:
                return person
                
        return -1
