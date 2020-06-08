class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N=len(nums)
        A=[-float('inf')]+nums+[float('inf')]
        cnt=0
        for i in range(N):
            if A[i]>A[i+1]:
                cnt+=1
                if A[i-1]>A[i+1] and A[i]>A[i+2]:
                    return False
            if cnt>1:
                return False
        return True
        
