class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        index_set = set()
        for i in range(len(nums)):
            index_set.add(i)
        
        for i in range(len(nums)):
            cur_product = 1
            for j in index_set:
                if i != j:
                    cur_product = cur_product * nums[j]
            result.append(cur_product)
        return result