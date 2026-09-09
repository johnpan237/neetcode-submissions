class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curArea = (r - l) * min(heights[l], heights[r])

            maxArea = max(maxArea, curArea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

        # Time Complexity: O(n)
        # Space Complexity: O(1)