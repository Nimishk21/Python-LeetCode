class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        b=len(B)//len(A)+1
        for i in range(1,b+2):
            if B in i*A:
                return i
        return -1
        
        
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a=A
        count=0
        while True:
          if B in a:
              return count+1
          if len(A)*count>len(B):
              return -1
          a+=A
          count+=1
            
