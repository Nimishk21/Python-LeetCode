class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)-1
        while(n>=0):
          if digits[n]!=9:
              digits[n]+=1
              return digits
           else:
              digits[n]=0
              n-=1
        if n==-1:
          digits=[1]+digits
          return digits
