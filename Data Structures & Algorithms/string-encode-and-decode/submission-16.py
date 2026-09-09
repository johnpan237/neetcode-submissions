class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index < len(s):
            j = index
            while s[j] != '#':
                j += 1
            length = int(s[index:j])
            res.append(s[j + 1:j + 1 + length])
            index = j + 1 + length
        return res