class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res, cur = [], []

        def dfs(idx, word):
            if idx == len(s):
                res.append(" ".join(cur))
                return
            
            for i in range(idx, len(s)):
                word += s[i]

                if word in wordSet:
                    cur.append(word)
                    dfs(i+1, "")
                    cur.pop()

        dfs(0, "")
        return res