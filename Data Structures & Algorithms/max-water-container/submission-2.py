class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result

# Time = O(n), Space = O(1)


        