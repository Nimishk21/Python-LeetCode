class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        r=0
        if k>=0:
            c=collections.Counter(nums)
            for i in c:
                if (k==0 and c[i]>1) or (k!=0 and i+k in c):
                    r+=1
         return r
