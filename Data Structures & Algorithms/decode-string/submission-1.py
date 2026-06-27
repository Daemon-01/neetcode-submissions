class Solution:
    def decodeString(self, s: str) -> str:
        stack = collections.deque()
        curNum = 0
        curStr = ""

        for char in s:
            if char.isdigit():
                # converts the multi digits numbers
                curNum = curNum * 10 + int(char)
            elif "[" == char:
                # push the prev sub-problem into the stack
                stack.append((curStr,curNum))
                curStr, curNum = "", 0
            elif char == "]":
                # form the new curr String
                prevStr , prevNum = stack.pop()
                curStr = prevStr + curStr*prevNum
            else:
                # adds the normal char
                curStr += char

        return curStr
