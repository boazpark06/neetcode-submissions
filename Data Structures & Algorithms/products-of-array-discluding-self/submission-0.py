class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        leftPass = 1

        for i in range(len(nums)):
            result[i] = leftPass
            leftPass *= nums[i]
        
        rightPass = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= rightPass
            rightPass *= nums[i]
        
        return result

# Time = O(n), Space = O(1) extra space, O(n) output array
        

        