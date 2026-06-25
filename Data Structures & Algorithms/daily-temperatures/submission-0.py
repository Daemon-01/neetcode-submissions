class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        idx = collections.deque()

        for i in range(len(temperatures)):
            while idx and temperatures[idx[-1]] < temperatures[i]:
                res[idx[-1]] = i - idx[-1]
                idx.pop()
            idx.append(i)
        return res