class Solution:
    import re
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr=re.findall(r"[a-zA-Z]+",paragraph.lower())
        count=collections.Counter(arr)
        
        for key,value in count.most_common():
            if key not in banned:
                return key
        return[]
        
        
