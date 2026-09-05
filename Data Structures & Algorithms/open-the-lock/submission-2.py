class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(["0000", 0]) # [lock, steps]
        visit = set(deadends)

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) 
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10) 
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res

        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, steps+1])
        return -1