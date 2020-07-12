class Solution:
    def longestPalindrome(self, s):
        cnt=collections.Counter(s)
        sign=False
        ans=0
        for i in cnt.values():
            if i%2==0:
                ans+=i
            elif i%2==1:
                ans+=i-1
                sign=True
         if sign:
            ans+=1
         return ans
