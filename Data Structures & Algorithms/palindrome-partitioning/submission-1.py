class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(0, [], res, s)
        return res

def is_palindrome(sub):
    return sub == sub[::-1]

def backtrack(start, path, res, s):
    # If we are at the end of the string, add the current path to results
    if start == len(s):
        res.append(path[:])
        return
    # Explore subsequent partitions
    for end in range(start, len(s)):
        # Consider substring s[start:end+1]
        if is_palindrome(s[start:end+1]):
            # Choose
            path.append(s[start:end+1])
            # Explore further with updated path
            backtrack(end+1, path, res, s)
            # Un-choose (backtrack)
            path.pop()        