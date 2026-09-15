class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        elif nums[m] > target:
            return self.binary_search(l, m - 1, nums, target)
