class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str: return False
        str1=str.split(' ')
        dict1={}
        for x,y in zip(pattern,str1):
            if x in dict1:
                if dict1[x]!=y:
                    return False
            elif y in dict1.values():
                return False
            else:
                dict1[x]=y
        return True
        
 class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
          def numlst(pattern):
              d={}
              for i in range(len(pattern)):
                  if pattern[i] not in d:
                      d[pattern[i]]=i
                  pattern[i]=d[pattern[i]]
              return pattern
          pattern,str=list(pattern),str.split()
          return numlst(pattern)==numlst(str)
