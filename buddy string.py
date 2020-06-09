#method 1:
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        elif A==B:
            return len(set(A)) != len(A)
        diff_char=[(a,b) for a,b in zip(A,B) if a!=b]
        return len(diff_char)==2 and diff_char[0][0]==diff_char[1][1] and diff_char[0][1]==diff_char[1][0]
        
        
