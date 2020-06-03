#method 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        k=len(strs[0])
        for s in strs[1:]:
            i=0
            while i<min(k,len(s)) and s[i]==strs[0][i]:
                i=i+1
            k=i
        return strs[0][:k]
      
#method 2:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        strs.sort()
        p=""
        for x,y in zip(strs[0],strs[-1]):
            if x==y:
                p+=x
            else:
                break
        return p
