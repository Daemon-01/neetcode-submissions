class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque() # index

        for i in range(len(nums)):
            # pop the left most when window moves
            if dq and dq[0] == i-k:
                dq.popleft()
            # remove any smaller elements before adding
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            
            if i >= k-1:
                res.append(nums[dq[0]])
        return res