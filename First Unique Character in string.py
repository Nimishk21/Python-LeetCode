class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=collections.Counter(s)
        for i,ch in enumerate(s):
            if c[ch]==1:
                return i
        return -1
