class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = {}

        for i in nums:
            myHash[i] = myHash.get(i, 0) + 1
        
        sortedNums = sorted(myHash, key = myHash.get, reverse = True)

        return sortedNums[:k]
        