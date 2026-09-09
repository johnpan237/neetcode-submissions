class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing_nums = set()

        for num in nums:
            if num in existing_nums:
                return True
            existing_nums.add(num)
        
        return False