class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if hash_map[complement]:
                return [hash_map[complement], i + 1]
            hash_map[numbers[i]] = i + 1
        
        return []