class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        curLen = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while(l<r and s[r] in seen):
                seen.remove(s[l])
                l,curLen = l+1,curLen-1
            seen.add(s[r])
            curLen += 1
            maxLen = max(maxLen,curLen)
        return maxLen