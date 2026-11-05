class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myHash = {}

        for i in nums:
            myHash[i] = myHash.get(i, 0) + 1
            if myHash[i] > len(nums) // 2:
                return i