class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = (l + r) // 2
            # Map 1D index back to 2D coordinates
            row, col = divmod(mid, cols)
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False