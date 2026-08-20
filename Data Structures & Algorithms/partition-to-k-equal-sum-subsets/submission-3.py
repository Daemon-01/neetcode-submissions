class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)

        if totalSum % k :
            return False
        # sorting in descending order to eliminate 
        # cases where elements can't be divided equally

        nums.sort(reverse=True)
        target = totalSum // k

        if nums[0] > target:
            return False

        targetSum = [0] * k

        def dfs(idx):
            # Base Cases 
            if idx == len(nums):
                return True

            for i in range(k):
                if nums[idx] + targetSum[i] <= target:
                    targetSum[i] += nums[idx]

                    if dfs(idx + 1):
                        return True
                    targetSum[i] -= nums[idx]

                if targetSum[i] == 0:
                    break
            return False
        return dfs(0)
            
