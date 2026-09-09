class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curArea = (r - l) * min(heights[r], heights[l])
            maximumArea = max(curArea, maximumArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maximumArea