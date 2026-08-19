class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)

        if totalSum % 4:
            return False
        
        target = totalSum // 4
        side = [0] * 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False
        
        def dfs(idx):
            # Base case
            if idx == len(matchsticks):
                return True
            
            for i in range(4):
                if side[i] + matchsticks[idx] <= target:
                    side[i] += matchsticks[idx]

                    if dfs(idx+1):
                        return True
                    side[i] -= matchsticks[idx]
                    if side[i] == 0:
                        break
            return False
        
        return dfs(0)