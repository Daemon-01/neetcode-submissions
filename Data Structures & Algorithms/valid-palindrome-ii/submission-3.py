class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                # Try skipping either l or r
                return isPalindromeRange(s, l + 1, r) or isPalindromeRange(s, l, r - 1)
            l, r = l + 1, r - 1
        return True


def isPalindromeRange(s: str, l: int, r: int) -> bool:
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True
