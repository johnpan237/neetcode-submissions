class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        # 2, 20, 4, 10, 3, 5

        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest