class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            result[key].append(s)
        return list(result.values())

        # Time: O(m * nlogn)
        # Space: O(n * m)
        