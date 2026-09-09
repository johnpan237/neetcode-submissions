class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        length = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)
        
        return length