class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)

        idx = 0

        for i in range(zeroes):
            nums[idx] = 0
            idx += 1
        
        for i in range(ones):
            nums[idx] = 1
            idx += 1
        
        for i in range(twos):
            nums[idx] = 2
            idx += 1
        
        return nums
        