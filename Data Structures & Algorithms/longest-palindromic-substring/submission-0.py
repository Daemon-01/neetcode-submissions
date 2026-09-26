class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1

        def cut(left:int, right:int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
        for i in range(len(s)):
            odd = cut(i, i)
            even = cut(i, i+1)
            cur = max(odd, even)

            if cur > max_len:
                max_len = cur
                start = i - (cur-1) // 2
        return s[start:start+max_len]