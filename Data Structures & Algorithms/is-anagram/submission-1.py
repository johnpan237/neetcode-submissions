class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        # return sorted(s) == sorted(t)
        # Time Complexity: O(nlog(n))
        # Space Complexity: O(1)