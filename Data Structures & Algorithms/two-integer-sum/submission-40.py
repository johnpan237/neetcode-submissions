class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in hashMap:
                return [hashMap[other_num], i]
            hashMap[num] = i
        
        return -1