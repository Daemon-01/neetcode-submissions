class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)

        if n != m:
            return False
            
        hash_s = {}
        for i in range(0,len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0) + 1

        for i in range(0,len(t)):
            if t[i] in hash_s and hash_s[t[i]] > 0:
                hash_s[t[i]] -= 1
            else:
                continue

        for val in hash_s.values():
            if val != 0:
                return False
        return True