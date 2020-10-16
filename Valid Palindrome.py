class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]', '', str(s).lower())
        return s[::-1] == s
    
#method 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=""
        for i in s:
            if i.isalnum()==True:
                str1+=i
        str2=str1[::-1]
        if str1.lower()==str2.lower():
            return True
        else:
            return False
