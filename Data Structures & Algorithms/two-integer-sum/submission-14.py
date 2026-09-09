class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in hashMap:
                return [hashMap[num2], i]
            hashMap[num1] = i
        
        return