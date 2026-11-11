class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Step 1: Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Group numbers by frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Iterate from highest frequency
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

# Time = O(n), Space = O(n)
        