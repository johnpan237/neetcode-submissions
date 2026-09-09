class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a, ... , z
            for c in s:
                count[ord(c) - ord('a')] += 1
            result_map[tuple(count)].append(s)
        return result_map.values()