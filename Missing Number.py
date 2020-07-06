class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set=set(nums)
        n=len(nums_set)
        for number in range(n):
            if number not in nums_set:
                return number
                
class Solution:
    def missingNumber(self, nums: List[int]) -> int:\
        sum=len(nums)*(len(nums)+1)//2
        sum_nums=sum(nums)
        return sum-sum_nums
