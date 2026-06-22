class Solution:
    def calPoints(self, A: List[str]) -> int:
        score = collections.deque()
        for op in A:
            if op == "C":
                score.pop()
            elif op == "D":
                score.append(2*score[-1])
            elif op == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(op))
        return sum(score)