class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for key in strs:
            sort = tuple(sorted(key))
            if sort in group:
                group[sort].append(key)
            else:
                group[sort] = [key]
        
        result = list(group.values())
        return result
        