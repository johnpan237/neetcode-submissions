class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count character frequencies in t
        char_need = Counter(t)
        # Counter to track current fulfillment in the sliding window
        window_count = {}
        # To keep a count of how many unique characters are fully satisfied
        have, need = 0, len(char_need)

        # Result window length and indices
        res = [float("inf"), None, None]

        # Left pointer of window
        left = 0

        # Expand the window with right pointer
        for right in range(len(s)):
            # Current character to process
            char = s[right]
            # Update count in current window
            window_count[char] = window_count.get(char, 0) + 1

            # Check if character's count is satisfied
            if char in char_need and window_count[char] == char_need[char]:
                have += 1

            # Try to contract from left while valid
            while have == need:
                # Update the result based on the current window size
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]

                # Attempt to contract by moving left pointer
                window_count[s[left]] -= 1
                if s[left] in char_need and window_count[s[left]] < char_need[s[left]]:
                    have -= 1
                left += 1

        return s[res[1]:res[2] + 1] if res[0] != float("inf") else ""