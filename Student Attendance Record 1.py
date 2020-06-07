#method 1
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1 or 'LLL' in s:
            return False
        else:
            return True

#method 2
class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        x=False
        for i in range(0,len(s)):
            if s[i]=='A':
                count+=1
        if 'LLL' in s or count>1:
            return False
        else:
            return True
        
        
        
