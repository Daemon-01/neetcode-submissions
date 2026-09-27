class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return n

        def expand(left:int, right:int):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        odd, even = 0, 0
        for i in range(n):
            odd += expand(i,i)
            even += expand(i,i+1)
        return (odd+even)