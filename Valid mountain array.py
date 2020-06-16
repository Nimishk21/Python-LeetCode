class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0
        if N<3 or A[0]>=A[1]:
            return False
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
    
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A)<3 or A[0]>=A[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(A)):
            if uphill:
                if A[i-1]>=A[i]:
                    uphill = False
            if not uphill:
                if A[i-1]<=A[i]:
                    return False
        return not uphill    
    
