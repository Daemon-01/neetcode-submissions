class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [p for p in path.split("/") if p]
        stack = collections.deque()

        for char in parts:
            if char == ".." and stack:
                stack.pop()
            elif char != "." and char != "..":
                stack.append(char)
        return "/" + "/".join(stack)
        