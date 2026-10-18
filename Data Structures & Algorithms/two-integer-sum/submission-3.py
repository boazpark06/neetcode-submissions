class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #compare every pair of elements excluding same indexs ex. (0,0)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        