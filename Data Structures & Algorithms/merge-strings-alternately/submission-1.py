class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) if len(word1) <= len(word2) else len(word2)
        mergedString = ""
        lastidx = 0
        for i in range(n):
            mergedString += word1[i] + word2[i]
            lastidx = i+1
        mergedString += word1[lastidx:]
        mergedString += word2[lastidx:]
        return mergedString