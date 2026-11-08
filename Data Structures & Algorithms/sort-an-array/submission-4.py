import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums

            pivot = random.choice(nums)

            left = []
            right = []
            middle = []

            for i in nums:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                else:
                    middle.append(i)
            return quicksort(left) + middle + quicksort(right) 
        return quicksort(nums)       

        