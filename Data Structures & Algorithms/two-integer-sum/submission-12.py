class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in myHash:
                return [myHash[diff], i]
            myHash[n] = i
        