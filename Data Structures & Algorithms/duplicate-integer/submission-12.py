class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in nums:
            if i not in mySet:
                mySet.add(i)
            else:
                return True
        return False

        