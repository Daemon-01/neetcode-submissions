class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(idx, currentXor):

            if idx == len(nums):
                return currentXor
            
            include = dfs(idx+1, currentXor^nums[idx])

            exclude = dfs(idx+1, currentXor)

            return include + exclude
        
        return dfs(0, 0)