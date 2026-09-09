class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle_index = (l + r) // 2

            if target > nums[middle_index]:
                l = middle_index + 1
            elif target < nums[middle_index]:
                r = middle_index - 1
            else:
                return middle_index
        
        return -1

        # Time Complexity: O(log(n))
        # Space Complexity: O(1)