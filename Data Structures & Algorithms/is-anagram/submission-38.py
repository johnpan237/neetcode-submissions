class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted(s))
        print(sorted(t))
        return sorted(s) == sorted(t)