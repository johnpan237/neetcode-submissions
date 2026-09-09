class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a -> index 0, ..., z -> index 25
            for c in s:
                # a = 80, 80 - 80 = 0
                # b = 81, 81 - 80 = 1
                count[ord(c) - ord('a')] += 1
            anagrams_map[tuple(count)].append(s)
        
        return anagrams_map.values()