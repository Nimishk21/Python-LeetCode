class Solution:
    from collections import Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1=Counter(ransomNote)
        cnt2=Counter(magazine)
        for c in cnt1.keys():
            if cnt1[c]>cnt2[c]:
                return False
        return True
        
 class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransom=collections.Counter(ransomNote)
        freq_magazine=collections.Counter(magazine)
        return not(freq_ransom-freq_magazine)      
       
