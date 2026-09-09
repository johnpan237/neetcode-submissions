class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in hashMap:
                return [hashMap[num2], i]
            hashMap[num] = i
        
        return -1