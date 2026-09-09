class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        
        return True
        # Time Complexity: O(S+T)
        # Space Complexity: O(S+T)


        # return Counter(s) == Counter(t)
        # Time Complexity: O(S+T) where S is the size of s, and T is the size of t
        # Space Complexity: O(S+T) where S is the size of s, and T is the size of t
        # This approach does exactly what I do above

        # return sorted(s) == sorted(t)
        # Time Complexity: O(nlog(n))
        # Space Complexity: O(1)