class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        
        for i, n in enumerate(nums):
            myHash[n] = i
        
        for i, n in enumerate(nums):
            diff = target - nums[i]
            # if diff in myHash and diff is not same index as i
            if diff in myHash and myHash[diff] != i:
                return [i, myHash[diff]]
       
                    

        