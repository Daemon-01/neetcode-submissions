class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderMap = {char : i for i, char in enumerate(order)}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1] 

            minLen = min(len(word1), len(word2))
            diff = False

            for j in range(minLen):
                if word1[j] != word2[j]:
                    if orderMap[word1[j]] > orderMap[word2[j]]:
                        return False
                    diff = True
                    break
            
            if not diff:
                if len(word1) > len(word2):
                    return False
        return True
