class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()

        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            s2_count[s2[i]] += 1

            if i >= len(s1):
                if s2_count[s2[i - len(s1)]] > 1:
                    s2_count[s2[i - len(s1)]] -= 1
                else:
                    del s2_count[s2[i - len(s1)]]
            
            if s1_count == s2_count:
                return True

        return False
        # Time Complexity: O(26 * n)
        # Space Complexity: O(n)

       
