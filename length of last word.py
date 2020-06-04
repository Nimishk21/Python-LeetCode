class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or s.isspace():
            return 0
        else:
            l1=s.split()
            return(len(l1[-1]))
