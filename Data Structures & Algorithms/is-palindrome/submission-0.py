class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_str = ''
        for c in s:
            if c.isalnum():
                result_str += c.lower()
        
        return result_str == result_str[::-1]

