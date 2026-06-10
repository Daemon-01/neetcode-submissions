class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # call helper with indices
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: List[int], low: int, high: int):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums: List[int], low: int, mid: int, high: int):
        # temporary buffer only for this merge
        temp = []
        i, j = low, mid + 1

        while i <= mid and j <= high:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        # add leftovers
        temp.extend(nums[i:mid+1])
        temp.extend(nums[j:high+1])

        # copy back into nums
        nums[low:high+1] = temp
