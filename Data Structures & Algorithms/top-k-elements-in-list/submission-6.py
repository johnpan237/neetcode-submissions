class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # you are not repeating this n times every time, so at the end is n+n = 2n
                result.append(n)
                if len(result) == k:
                    return result
        return

        # Time Complexity: O(n)
        # Space Complexity: O(n)