class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(idx, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            for i in range(idx, n+1):
                #include the current number
                cur.append(i)
                dfs(i+1, cur)

                #exclude the current element
                cur.pop()
        dfs(1,cur)
        return res