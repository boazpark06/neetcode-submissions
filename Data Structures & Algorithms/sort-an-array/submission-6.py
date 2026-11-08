class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(size, i):
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                # Find the largest of parent and children
                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right

                # Stop if the parent is already the largest
                if largest == i:
                    break

                # Swap and continue down the heap
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        # 1. Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # 2. Sort the array
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums

        
        