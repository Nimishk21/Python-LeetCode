class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<2: return False
        primes=[2,3,5,7,13,17,19,31]
        for prime in primes:
            if (2**(prime-1))*((2**prime)-1)==num:
                return True
        return False
        
        
        
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total=0
        for i in range(1,num):
            if num%i==0:
                total+=i
        return total==num
