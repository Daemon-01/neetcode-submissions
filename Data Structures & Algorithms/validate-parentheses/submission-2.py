class Solution:
    def isValid(self, s: str) -> bool:
        brace = collections.deque()
        
        for br in s:
            if br =="(" or br == "[" or br == "{":
                brace.append(br)
            else:
                if len(brace) == 0:
                    return False
                elif (brace[-1] == "{" and br == "}" or
                   brace[-1] == "(" and br == ")" or 
                   brace[-1] == "[" and br == "]") :
                   brace.pop()
                else:
                    return False
        return len(brace) == 0