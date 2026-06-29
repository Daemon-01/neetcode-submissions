# Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        left, right = [-1]*n, [n]*n
        stack = []

        # Nearest Smaller to Left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()

        # Nearest Smaller to Right
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        for i in range(n):
            width = right[i] - left[i] -1
            area = heights[i] * width
            maxArea = max(maxArea,area)
        return maxArea