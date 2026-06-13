class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        # Step 1: Cleanup
        for i in range(len(A)):
            if A[i] <= 0 or A[i] > len(A):
                A[i] = 0

        # Step 2: Mark presence
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                idx = val - 1
                if A[idx] > 0:
                    A[idx] = -A[idx]        # mark as seen
                elif A[idx] == 0:
                    A[idx] = -(len(A) + 1)  # special marker

        # Step 3: Find first missing
        for i in range(len(A)):
            if A[i] >= 0:
                return i + 1
        return len(A) + 1
