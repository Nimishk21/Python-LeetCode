class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        if s==s[::-1]:
            return True
         while start<end:
              if s[start]==s[end]:
                  start+=1
                  end-=1
              else:
                  v1=s[start+1:end+1]
                  v2=s[start:end]
                  return v1==v1[::-1] or v2==v2[::-1]
         return True
       
       
 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
         start,end=0,len(s)-1
         while s[start]==s[end]:
            start+=1
            end-=1
         new_s=s[start+1:end+1]
         if new_s=new_s[::-1]:
            return True
         new_s=s[start:end]
         if new_s==new_s[::-1]:
            return True
         return False
         
