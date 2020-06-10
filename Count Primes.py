class Solution:
    def countPrimes(self, n: int) -> int:
        mark=[True for i in range(n+1)]
        p=2
        while p*p<n:
            if mark[p]=True:
                for i in range(p*p,n,p):
                    mark[i]=False
            p=p+1
        count=0
        for i in range(2,n):
            if mark[i]==True:
              count+=1
        return count
        
        
class Solution:
    def countPrimes(self, n: int) -> int:
        marked=[True]*n
        for i in range(2,n):
            if i>2 and i%2==0:
              marked[i]=False
              continue
            for j in range(i*i,n,i):
                marked[j]=False
         count=0
         for i in range(2,n):
            if marked[i]:
                count+=1
         return count
