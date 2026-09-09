class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if hashmap[complement]:
                return [hashmap[complement], i + 1]
            hashmap[numbers[i]] = i + 1
        
        return []