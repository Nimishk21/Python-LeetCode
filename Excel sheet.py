class Solution:
    def convertToTitle(self, n: int) -> str:
        letters=list(string.ascii_uppercase)
        result=""
        while(n!=0):
            n,r=divmod(n-1,26)
            result=letters[r]+result
         return result
