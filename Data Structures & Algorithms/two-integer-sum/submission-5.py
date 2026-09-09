class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        index1, index2 = None, None

        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - nums[i]

            if num2 in nums_map:
                index1, index2 = i, nums_map[num2]
            
            nums_map[num1] = i
        
        return sorted([index1, index2])