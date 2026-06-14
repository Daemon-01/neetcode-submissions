class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while(l<r):
            while l<r and not s[l].isalnum():
                l = l+1 
            while l<r and not s[r].isalnum():
                r = r-1

            if l<r:
                if s[l].lower() != s[r].lower():
                    return False
            l,r = l+1,r-1
        return True