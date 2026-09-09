class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1, index2 = None, None
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index1, index2 = i, j
        
        return [index1, index2]