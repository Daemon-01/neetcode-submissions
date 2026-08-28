class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Map each letter to its position in the alien order
        order_map = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Compare characters of adjacent words
            for j in range(min(len(word1), len(word2))):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    # If character in word1 has a higher rank than word2, it's invalid
                    if order_map[c1] > order_map[c2]:
                        return False
                    break
            else:
                # If no mismatch found, check if word1 is longer than word2
                if len(word1) > len(word2):
                    return False
                    
        return True
