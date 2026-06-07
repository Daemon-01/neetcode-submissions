class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCPrefix = strs[0]

        for i in range(1,len(strs)):
           word = strs[i]
           for j in range(0,len(LCPrefix)):
              if j < len(word) and LCPrefix[j] == word[j]:
                 continue
              else:
                 LCPrefix = LCPrefix[0:j]
                 break
        if LCPrefix == " " :
           return LCPrefix
        return LCPrefix
