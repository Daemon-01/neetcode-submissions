class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        low , high = 0 , len(nums)
        mid = low + (high-low)//2
        left , right = self.sortArray(nums[0:mid]) , self.sortArray(nums[mid:high])
        return self.mergeSorted(left , right)
    
    def mergeSorted(self,left:List[int],right:List[int]) -> List[int]:
        sortedArray = []
        i = j = 0

        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                sortedArray.append(left[i])
                i += 1
            else:
                sortedArray.append(right[j])
                j += 1
        sortedArray.extend(left[i:])
        sortedArray.extend(right[j:])
        return sortedArray
