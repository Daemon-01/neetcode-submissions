class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxCount = 0
        res = 0
        l =0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            maxCount = max(maxCount,count[s[r]])

            while (r-l+1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res        